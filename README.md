# FreeEduFetch API Documentation

Welcome to the FreeEduFetch API documentation. FreeEduFetch is an API that provides information about free courses from Udemy. The API is implemented in Python and hosted on Render.

## API Endpoints

- **JSON**: [https://free-edu.onrender.com/api/coupons/json](https://free-edu.onrender.com/api/coupons/json)
- **XML**: [https://free-edu.onrender.com/api/coupons/xml](https://free-edu.onrender.com/api/coupons/xml)
- **YAML**: [https://free-edu.onrender.com/api/coupons/yaml](https://free-edu.onrender.com/api/coupons/yaml)
- **TXT**: [https://free-edu.onrender.com/api/coupons/txt](https://free-edu.onrender.com/api/coupons/txt)
- **CSV**: [https://free-edu.onrender.com/api/coupons/csv](https://free-edu.onrender.com/api/coupons/csv)
#### Or you can just use as [https://free-edu.onrender.com/](https://free-edu.onrender.com/)
##### It will show like this - 
[![Screenshot-2023-11-22-111402.png](https://i.postimg.cc/g2Nc6Xpp/Screenshot-2023-11-22-111402.png)](https://postimg.cc/hXQRkGhZ)
## Data Formats

The FreeEduFetch API supports multiple data formats for your convenience:

- **JSON**: Use the `/api/coupons/json` endpoint to get data in JSON format.
- **XML**: Use the `/api/coupons/xml` endpoint to get data in XML format.
- **YAML**: Use the `/api/coupons/yaml` endpoint to get data in YAML format.
- **TXT**: Use the `/api/coupons/txt` endpoint to get data in plain text format.
- **CSV**: Use the `/api/coupons/csv` endpoint to get data in CSV format.

## Examples of Fetching Data

### Python

```python
import requests

url = "https://free-edu.onrender.com/api/coupons/json"
response = requests.get(url)
data = response.json()

# Use 'data' as needed
```

### Node.js
```javascript
const fetch = require('node-fetch');

const url = 'https://free-edu.onrender.com/api/coupons/json';
const response = await fetch(url);
const data = await response.json();

// Use 'data' as needed

```
### Java
```java
import java.net.URL;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;

public class FreeEduFetchExample {
    public static void main(String[] args) {
        try {
            URL url = new URL("https://free-edu.onrender.com/api/coupons/json");
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("GET");

            BufferedReader in = new BufferedReader(new InputStreamReader(conn.getInputStream()));
            String inputLine;
            StringBuilder content = new StringBuilder();

            while ((inputLine = in.readLine()) != null) {
                content.append(inputLine);
            }

            in.close();

            // Use 'content' as needed
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

```
### Go
```go
package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
)

func main() {
	url := "https://free-edu.onrender.com/api/coupons/json"
	response, err := http.Get(url)
	if err != nil {
		fmt.Println(err)
		return
	}
	defer response.Body.Close()

	body, err := ioutil.ReadAll(response.Body)
	if err != nil {
		fmt.Println(err)
		return
	}

	var data map[string]interface{}
	err = json.Unmarshal(body, &data)
	if err != nil {
		fmt.Println(err)
		return
	}

	// Use 'data' as needed
}

```
### TypeScript
```typescript
import axios from 'axios';

const url = 'https://free-edu.onrender.com/api/coupons/json';
const response = await axios.get(url);
const data = response.data;

// Use 'data' as needed

```
### Ruby
```ruby
require 'net/http'
require 'json'

url = URI.parse('https://free-edu.onrender.com/api/coupons/json')
http = Net::HTTP.new(url.host, url.port)
request = Net::HTTP::Get.new(url.request_uri)
response = http.request(request)

data = JSON.parse(response.body)
# Use 'data' as needed

```
### PHP
```php
$url = 'https://free-edu.onrender.com/api/coupons/json';
$response = file_get_contents($url);
$data = json_decode($response, true);

// Use '$data' as needed

```
### Swift
```swift
import Foundation

if let url = URL(string: "https://free-edu.onrender.com/api/coupons/json") {
    if let data = try? Data(contentsOf: url) {
        let json = try? JSONSerialization.jsonObject(with: data, options: [])
        if let dictionary = json as? [String: Any] {
            // Use 'dictionary' as needed
        }
    }
}

```
### C#
```c#
using System;
using System.Net.Http;
using System.Threading.Tasks;

class Program
{
    static async Task Main()
    {
        using (HttpClient client = new HttpClient())
        {
            string url = "https://free-edu.onrender.com/api/coupons/json";
            HttpResponseMessage response = await client.GetAsync(url);
            response.EnsureSuccessStatusCode();

            string responseBody = await response.Content.ReadAsStringAsync();
            // Use 'responseBody' as needed
        }
    }
}

```
##### Made with ❤️
