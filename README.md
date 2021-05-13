### Creating/registering user

> ```
> {
>   "data": {
>     "id": "null",
>     "type": "urban_area",
>     "attributes": [
>       {
>         "id": "integer",
>         "title": "string",
>         "min_salary": "float",
>         "max_salary": "float"
>       }
>     ]
>   }
> }

### Bad request or invalid credential per user post

> ```
> {
>   error: 'Bad Request for your parameter',
>   errors: "parameter is bad: #{reason}"
> }


### Response for Salary Page

>```
>{
>    'data': { 
>        'id': null,
>        'type': 'urban area'
>        'attributes': [
>            {  
>                'id': integer,
>                'title': string,
>                'min_salary': float,
>                'max_salary': float
>             }
>        ]
>     }
>}

### StackOverflow Microservice to Backend

> ```
> {
>  "data": [{
>    "id": "integer",
>    "type": "job_post",
>    "attributes":{
>      "title": "string",
>      "company": "string",
>      "category": "array(strings)",
>      "description": "string",
>      "location": "string",
>      "publish_date": "datetime",
>      "link": "string"
>      },
>      {...}
>   }]
> }
 

### session authentication

>```
>{ 
>    'email': string,
>    'password': string
>}
> 
> status: :ok

### Profile page

>```
>request
>
>{
>     'email': string,
>}
>
>response
>
>{
>    'data': { 
>        'id': null,
>        'type': 'user'
>        'attributes': {
>            'first_name': string,
>            'last_name': string,
>            'email': string,
>            'city': string,
>            'state': string (initial),
>            'zipcode': string,
>            'saved_jobs': [
>                {
>                    'job_title': string,
>                    'location': string,
>                    'company': string,
>                    'url': string
>                }
>            ]
>        }
>     }
>}

