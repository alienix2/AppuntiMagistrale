# Real vulnerabilities

## XSS (Cross Site Scripting)

XSS is a vulnerability that allows for the user to execute arbitrary code in a vulnerable web page. This can usually be performed only on a **poorly sanitized field**.

The most common POC for XSS is to inject `<script>alert(1)</script>` in a vulnerable field. This will execute the code and show an alert with the number 1.

*Note:* this is a perfect example of what a POC should be, an armless piece of code that shows that the vulnerability is real and that it can be exploited.

This kind of attack usually stems from the use of **php** which is very flawed.

XSS cannot be easily spotted by vulnerability scanners because it's hard to understand where the XSS might work and also how the data is handled by the different fields. Moreover many times the side effects of XSS are on a different page than the injectable one.

### Using an image

The XSS can also be performed by using an image. For instance we can use the syntax: `<img src=x onerror=alert(1)>`. This will execute the alert as we are sure that the error will be triggered.

### When can you use XSS

XSS can be used when the code is **tainted**. This means that the code is not sanitized and can be executed by the browser.
In general if there is no **tainted flow** in the code, you cannot use XSS. This means that a tainted flow is **necessary** but this doesn't mean that it is **sufficient**.

### Stored XSS vs reflected XSS

**Reflected XSS** is a type of XSS that is reflected in the URL. This means that the code is executed when the page is loaded. This is the classic type of XSS that was described above.

**Stored XSS** is a type of XSS that is stored in the database. This means that the code is stored in the database and executed when the page is loaded. This is usually done by using a **comment** or a **post**. This kind of XSS is often defined as more dangerous than reflected XSS.

## SQL injection

SQL injection is a vulnerability that allows the user to perform not intended actions on a database. *Note:* it's not important to actually use this kind of attacks only on SQL databases, most likely also **NoSQL** databases can be attacked using the same methodology by using the correct syntax.

### Basic SQL injection

A basic SQL injection on a field that performs something like: `"SELECT * FROM users WHERE user = '$user' AND pass = '$passwd'"` can be performed by injecting the following code in the user field: `admin' OR 1=1 --`. This will make the query to be executed as: `"SELECT * FROM users WHERE user = 'admin' OR 1=1 --' AND pass = '$passwd'"`. This will return all the users in the database. The `--` is used to comment the rest of the query.

### Blind SQL injection

This kind of SQLi doesn't return something directly. Still there are ways to verify if the SQLi actually worked or not. A very simple example are tainted flow that actually return something (not related to the input) different depending on the success or failure of the SQL call.

Another important attack that can be performed on blind SQLi spots are the one that rely on a **time oracle**.

Time oracle can also be used to perform **binary search** on the single letters of a value that we want to check if it exists or not. This is done by using the `SLEEP` command. For instance if we want to check if the user `admin` exists in the database we can use the following query: `"SELECT * FROM users WHERE user = 'admin' AND SLEEP(5)"`. If the user exists the query will take 5 seconds to execute, otherwise it will take less than 1 second.

Oracles in general can also be used to check for single characters, even if it needs a more complex query (and many tries with binary search). *Note:* you should rely on an automated software to generate the more complex query.
