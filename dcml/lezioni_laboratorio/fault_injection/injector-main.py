import csv
import json
import os.path
import random
import time

from tqdm import tqdm

from LoadInjector import LoadInjector, current_ms


def main_injector(
    max_n_obs: int,
    injectors: list,
    obs_interval_sec: int = 1,
    inj_duration_sec: int = 1,
    inj_cooldown_sec: int = 2,
    inj_probability: float = 0.2,
    verbose: bool = True,
):
    """
    Main function for monitoring
    :param inj_cooldown_sec: time to wait after an injection and before activating a new one (seconds)
    :param inj_duration_sec: duration of the injection (seconds)
    :param verbose: True if debug information has to be shown
    :param injectors: list of LoadInjector objects
    :param inj_probability: float number which represents a probability of an injection to take place
    :param obs_interval_sec: seconds in between two observations (seconds)
    :param max_n_obs: maximum number of observations
    :return: list of dictionaries containing activations of injections
    """

    # Injection Loop
    print("Injector Started. Active for %d times" % max_n_obs)
    current_inj = None
    inj_timer = 0
    cycle_ms = obs_interval_sec * 1000

    if injectors is not None and len(injectors) > 0:
        for obs_id in tqdm(range(max_n_obs), desc="Injector Progress Bar"):
            start_ms = current_ms()
            # If there are no active injections and no cooldown
            # If there is enough time before end of campaign
            # If probability activates
            if (
                current_inj is None
                and inj_timer == 0
                and ((max_n_obs - obs_id - 1) * cycle_ms > inj_duration_sec)
                and (random.randint(0, 999) / 999.0) <= inj_probability
            ):
                # Randomly chooses an injector and performs injection
                while current_inj is None:
                    inj_index = random.randint(0, len(injectors) - 1)
                    if not injectors[inj_index].is_injector_running():
                        current_inj = injectors[inj_index]
                if verbose:
                    print("Injecting with injector '%s'" % current_inj.get_name())

                # Starts the injection thread
                current_inj.inject()
                inj_timer = inj_duration_sec + inj_cooldown_sec

            # Sleep to synchronize with cycle time
            sleep_s = (cycle_ms - (current_ms() - start_ms)) / 1000.0
            if sleep_s > 0:
                time.sleep(sleep_s)

            # Managing cooldown
            inj_timer = inj_timer - cycle_ms if inj_timer > 0 else 0
            if inj_timer < inj_cooldown_sec:
                current_inj = None

    else:
        print("No injectors were set for this experimental campaign")

    activations = []
    for inj in injectors:
        inj_log = inj.get_injections()
        if inj_log is not None and len(inj_log) > 0:
            new_inj = [dict(item, inj_name=inj.get_name()) for item in inj_log]
            activations.extend(new_inj)
            if verbose:
                print(
                    "Injections with injector '"
                    + str(inj.get_name())
                    + "': "
                    + str(len(new_inj))
                )

    return activations


def read_injectors(json_object, inj_duration: int = 2, verbose: bool = True):
    """
    Method to read a JSON object and extract injectors that are specified there
    :param inj_duration: number of subsequent observations for which the injection takes place
    :param json_object: the json object or file containing a json object
    :param verbose: True is debug information has to be shown
    :return: a list of available injectors
    """
    try:
        json_object = json.loads(json_object)
    except ValueError:
        if os.path.exists(json_object):
            with open(json_object) as f:
                json_object = json.load(f)
        else:
            print("Could not parse input %s" % json_object)
            json_object = None
    json_injectors = []
    if json_object is not None:
        # Means it is a JSON object
        json_injectors = []
        for job in json_object:
            job["duration_ms"] = inj_duration
            new_inj = LoadInjector.fromJSON(job)
            if new_inj is not None and new_inj.is_valid():
                # Means it was a valid JSON specification of an Injector
                json_injectors.append(new_inj)
                if verbose:
                    print("New injector loaded from JSON: %s" % new_inj.get_name())

    return json_injectors


if __name__ == "__main__":
    """
    Entry point for the Injector
    """

    # General variables
    out_folder = "output_folder"
    inj_filename = "inj_info.csv"
    inj_json = "input_folder/injectors_json.json"
    inj_duration_sec = 2
    exp_duration = 20

    # Extracting definitions of injectors from input JSON
    injectors = read_injectors(inj_json, inj_duration=inj_duration_sec * 1000)

    # Calling injection routine
    inj_timestamps = main_injector(
        max_n_obs=exp_duration,
        injectors=injectors,
        obs_interval_sec=1,
        inj_duration_sec=inj_duration_sec,
        inj_cooldown_sec=2,
        inj_probability=0.4,
        verbose=False,
    )

    # Checking of out_folder already exists: if yes, delete
    if not os.path.exists(out_folder):
        os.mkdir(out_folder)

    # Checking of inj_filename already exists: if yes, delete
    inj_filename = os.path.join(out_folder, inj_filename)
    if os.path.exists(inj_filename):
        os.remove(inj_filename)

    # Print injection list
    with open(inj_filename, "w", newline="") as myFile:
        writer = csv.writer(myFile)
        keys = ["start", "end", "inj_name"]
        writer.writerow(keys)
        for dictionary in inj_timestamps:
            writer.writerow([str(dictionary[d_key]) for d_key in keys])
