# Marshall data in Go

The main language used for marshalling is JSON. In this regard the GO standard library includes `encoding\json` to work with JSON.

## TAGS

*Example:*

```Go
type UseAll struct {
  Name string `json:"name"`
  Surname string `json:"surname"`
  Year int `json:"crated"`
}
```

In JSON this will become:

 ```json
 {
   "name": "John",
   "surname": "Doe",
   "created": 2021
 }
 ```

To marshal data we use the `json.Marshal` function. This function returns a byte slice and an error. The byte slice is the JSON representation of the data.

To unmarshal data we use the `json.Unmarshal` function. This function takes a byte slice and a pointer to a struct. The function will fill the struct with the data from the byte slice.

*Example:*

```Go
str := `{"name": "John", "surname": "Doe", "created": 2021}`
jsonRecord := []byte(str)
temp := UseAll{}
err := json.Unmarshal(jsonRecord, &temp)

if err != nil {
  fmt.Println(err)
} else {
  fmt.Println("Data type: %T with value: %v\n", temp, temp)
}
```

We can make the encoder ignore private and empty fields.
*Example:*
  
```Go
type UseAll struct {
  Name string `json:"name"`
  Surname string `json:"surname"`
  Year int `json:"crated"`
  private string
}
```

## Writing

To write data in JSON we use the `json.NewEncoder` function. This function takes an `io.Writer` and returns a pointer to an `Encoder`. The `Encoder` has the method `Encode` that takes an interface and writes it to the `io.Writer`. Usually we want to directly get something from the net and read it in our code.

*Example:*

```Go
package main

type Data struct {
  Key string 'json:"key"'
  Data string 'json:"data"'
}

type DataArray []Data

func main() {
  data := DataArray{
    Data{"key1", "data1"},
    Data{"key2", "data2"},
  }

  enc := json.NewEncoder(os.Stdout)
  enc.Encode(data)
}
```
*Note:* the difference between `json.Marshal` and `json.NewEncoder` is that the first one returns a byte slice and the second one writes directly to the `io.Writer` and therefore allows to directly get an array.
