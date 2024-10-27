# XML and YAML in Go

## XML

In Go standard library there are functions to parse XML files. The package `encoding/xml`. Nowaday, XML is not so used as JSON, but it is still used in some contexts, in particular if we need to work with legacy code.

The idea is similar to what happens with the JSON package. We have to define a struct that represents the XML file and then we can use the `xml.Unmarshal` and `xml.Marshall` functions to work with the XML file. We also have the concept of tags.

*Example of XML handling:*

```go
type Address struct {
  City, Country string
}
type Employee struct {
  XMLName xml.Name `xml:"employee"`
  ID int `xml:"id,attr"`
  FirstName string `xml:"name>first"`
  LastName string `xml:"name>last"`
  Height float32 `xml:"height,omitempty"`
  Address
  Comment string `xml:",comment"`
}
```

*Writing data:*

```go
r := Employee{ID: 7, FirstName: "Mihalis", LastName: "Tsoukalos"}
r.Comment = "Technical Writer + DevOps"
r.Address = Address{"SomeWhere 12", "12312, Greece"}
output, err := xml.Marshal(r)
if err != nil {
  fmt.Println("Error:", err)
}
output = []byte(xml.Header + string(output))
fmt.Printf("%s\n", output)
```

*Reading data:*

```Go
// ...
r = Employee{}
err := xml.Unmarshal(input, &tempXML)
// check err for errors
fmt.Printf("%v\n", r)
```

## YAML

For YAML in Go the use of an external library is needed. The most popular are:

- <https://github.com/go-yaml/yaml>
- <https://githug..com/goccy/go-yaml>

*Note:* check yaml.go for examples
