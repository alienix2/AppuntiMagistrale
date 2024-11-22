# Estimating phase

This is a phase that is part of the planning phase.

## Effort duration and resources

When we talk about **Estimating**, we usually analyze 3 aspects:

- **Effort** needed for the activity to be completed
- **Resources** that are necessary to complete the work (we often talk about human resources in this case)
- **Duration** of the activity.

### Effort

The word **effort** is used to describe the amount of work needed to complete an activity. This should be a starting point. It' usually measured in **Work-days** (work-weeks, work-months). In this part we should be specific so we should also include the time needed for indirect activities.

### Resources

In this case we are talking about the resources that are needed to carry the work out. Usually a constraint is inserted, cause the resources are limited.

Resources are usually expressed thorough **manpower** which means the number of people that are needed to complete and what time they need to work at. (*I.e:* 1 person full time, 2 people at 50%).

There might be the need of material resources, which are usually expressed in terms of quantity. They are usually consumables, but they might not (*I.e:* I buy computer power from a server farm)

### Duration

The duration is the time needed to complete the activity. It's usually measured in days, weeks, and months.

The **calendar time** is different from the row duration. (*I.e:* 24h -> 3d of work cause people cannot work for more than 8 hours in a day).

Usually: 1 week = 5 days = 40 hours, 1 month = 20 days = 160 hours. In some countries we even have 1 week = 36 hours. We cannot think of having a work which needs 30*24h of work to be done in a month.

## Relation between the 3

### D = E/M

This assumption is very simplified. Usually we intend on using this formula to calculate D using E and M but it would be easy to do the opposite. Another formula to consider is: $M=\sum_{i=1}^Np_i$

*Note:* this formula is usually used to make decision but we shouldn't use this formula in order to decide that something should **definitely not be done**.

*Note:* some works cannot be divided in parallel, so we cannot use this formula as it is for every work. Hiring 300 people for a 300hours job doesn't mean that you will be done in 1 single day.

## Uncertainty in planning

Three practices that are usually followed in planning are:

- **Implicit padding:** which means that all the activities should have some extra time planned for them so that if a contingency happens it's no big deal.
- **Explicit padding:** which means that the contingency time is explicitly planned and written down in the activity. *Note:* this is usually better but a client that sees this kind of padding activity planned could think that this is just a waste of time. The days (total) that are spent doing the explicit padding are paid days and the client might argue with that. In that case is better to use implicit padding.
- **React and replan:** you don't put any padding but you are ready to change the plan if it's needed. *Note:* usually this strategy is only used as a last resort if the above weren't implemented well or weren't enough.

*Note:* replanning could be very costly, so you should first evaluate how much you can afford to change the plan. Also another important thing is to be clear with yourself and with the stakeholder on how you are dealing with contingency

*Note:* early delivery might also be an issue in some cases, that's because most of the time you still need to pay for the people that you hired for a longer time, which means that you will have to reallocate them somehow if you don't want to pay them for doing nothing.
