#GET https://cloudruntomysql-65075094468.us-central1.run.app/employees
#GET https://cloudruntomysql-65075094468.us-central1.run.app/employee/6

#POST https://cloudruntomysql-65075094468.us-central1.run.app/employee    or
#PUT https://cloudruntomysql-65075094468.us-central1.run.app/employee/2

Headers: Content-Type: application/json
Body (raw JSON):
{
  "name": "John Doe",
  "department": "Engineering",
  "salary": 75000
}

#DELETE https://cloudruntomysql-65075094468.us-central1.run.app/employee/8


