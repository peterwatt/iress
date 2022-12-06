# IRESS SRE challange
## Deploy an internet facing serverless application on AWS. The Lambda should be written in Python. The application needs to expose an endpoint which takes the city name as an input and returns the current weather

To deploy an internet facing serverless application on AWS, you would first need to create an AWS account if you don't already have one.

Next, you would need to create a new Lambda function using the AWS Management Console. You would select the Python runtime and provide the code for your application. This code would need to call an open source weather API (such as OpenWeatherMap) and return the current weather for the given city.

Once the Lambda function is created, you would need to create an API Gateway to expose the Lambda as a web service. You would configure the API Gateway to accept the city name as an input parameter and map it to the corresponding parameter in the Lambda function.

Next, you would need to deploy the API Gateway, which would make it available for use. You would then be able to access the endpoint using the provided URL and passing in the city name as a query parameter.

You would also need to configure the API Gateway to pass the city name as the city parameter to the Lambda function. This parameter would then be accessed in the event argument in the lambda_handler function.
You would also need to configure the necessary security and access control settings for the API Gateway and Lambda function to ensure that only authorized users can access the endpoint.

Overall, deploying an internet facing serverless application on AWS involves creating a Lambda function, creating an API Gateway, deploying the API Gateway, and configuring security and access controls.


This is a very basic example, and you may want to add additional logic or error handling to your code as needed.

## Which other services would you have preferred to include for resilience, scaling and security

If this were to be implemented in a production environment, I would recommend using additional AWS services for resilience, scaling, and security.

For resilience, I would recommend using Amazon Elasticache to cache the weather data. This would reduce the number of calls to the OpenWeatherMap API and improve the performance of the application. It would also provide a fallback in case the API is unavailable or slow.

For scaling, I would recommend using Amazon CloudWatch to monitor the usage of the Lambda function and API Gateway. If the usage exceeds a certain threshold, CloudWatch could automatically trigger a scale-out event to increase the number of instances of the Lambda function and API Gateway. This would ensure that the application can handle a large number of requests without performance degradation.

For security, I would recommend using Amazon Cognito to provide authentication and authorization for the application. Cognito would allow you to define user pools and assign permissions to different users or groups of users. This would ensure that only authorized users can access the endpoint and prevent unauthorized access.

Overall, using additional AWS services would improve the resilience, scalability, and security of the application in a production environment.

When deploying a microservice, it is important to expose basic metrics, set up monitoring and alerting, and implement a retry mechanism.

Basic metrics to expose, monitoring, alerting and retry mechanism for the microservice

For metrics, I would recommend exposing the following basic metrics:
•	Request count: the number of requests received by the microservice
•	Request latency: the time taken to process each request
•	Error rate: the percentage of requests that result in errors
•	Throughput: the number of requests per second that the microservice can handle

These metrics would provide a basic understanding of the performance and health of the microservice.

For monitoring and alerting, I would recommend using a tool such as Amazon CloudWatch. CloudWatch can be configured to collect and monitor the metrics exposed by the microservice, and to send alerts if certain thresholds are exceeded. For example, you could set up an alert to notify you if the error rate exceeds a certain percentage or if the request latency exceeds a certain value.

For the retry mechanism, I would recommend implementing an exponential backoff algorithm. This algorithm would retry failed requests with increasing intervals between each retry. For example, if a request fails, it could be retried after 1 second, then after 2 seconds, then after 4 seconds, and so on. This would allow the microservice to recover from temporary failures without overwhelming the system with a large number of retries.

Overall, exposing basic metrics, setting up monitoring and alerting, and implementing a retry mechanism would help ensure the reliability and performance of the microservice in a production environment.
## Chaos testing
To perform chaos testing on your Lambda function, you can use a tool like the Chaos Toolkit or Gremlin. These tools provide a framework for defining and executing chaos experiments, allowing you to define specific failure scenarios and observe how your function responds.
Here is an example of how you might use the Chaos Toolkit to perform chaos testing on your Lambda function:
1.	Install the Chaos Toolkit on your computer, following the instructions in the toolkit's documentation.
2.	Define a chaos experiment for your Lambda function. This will typically involve creating a YAML file that specifies the details of the experiment, such as the name of the function, the failure scenario to be tested, and the desired outcome of the experiment.
3.	Run the chaos experiment using the chaos run command, providing the path to the YAML file you created in the previous step. This will cause the specified failure scenario to be injected into your function, and the toolkit will observe how the function responds.
4.	Analyze the results of the experiment. The Chaos Toolkit will generate a report showing the details of the experiment, including any failures that occurred and how the function responded to those failures. You can use this information to identify areas where your function could be improved in terms of its resilience and ability to recover from failures.

## Acknowledgement
This document and the Python Lambda code were generated using ChatGTP at https://chat.openai.com/chat.

Peter Watt

5 December 2022


