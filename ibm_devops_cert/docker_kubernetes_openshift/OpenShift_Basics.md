---
markdown-version: v1
tool-type: instructional-lab
branch: lab-2822-instruction
version-history-start-date: '2022-12-15T12:28:15Z'
---
<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/cc201/images/IDSN-logo.png" width="200" alt="cognitiveclass.ai logo">

##

<div align="center"> <b>Glossary: OpenShift Basics</b> </div>
<br>

<table> 
<tr> 
<th width="30%">Term</th width="70%"><th>Definition</th> 
</tr> 

<tr> 
<td width="30%"><b>A/B testing</b></td> 
<td width="70%">Strategy is mostly used for testing new features in front-end applications. It is used to evaluate two versions of the application namely A and B, to assess which one performs better in a controlled environment. The two versions of the applications differ in terms of features and cater to different sets of users. Based on the interaction and responses received from the users such as feedback, you can choose one of the versions of the application that can be deployed globally into production. 
</tr> 

<tr> 
<td width="30%"><b>Build</b></td> 
<td width="70%">The process of transforming inputs into a resultant object. 
</tr>

<tr> 
<td width="30%"valign="top"><b>BuildConfig</b></td> 
<td width="70%">An OpenShift-specific object that defines the process for a build to follow. The build process makes use of the input sources and the build strategy. The BuildConfig is the blueprint, and the build is an instance of that blueprint.
</td> 
</tr> 

<tr> 
<td width="30%"valign="top"><b>Canary Deployments</b></td> 
<td width="70%">Aims to deploy the new version of the application by gradually increasing the number of users. The canary deployment strategy uses the real users to test the new version of the application. As a result, bugs and issues can be detected and fixed before the new version of the application is deployed globally for all the users.
</td> 
</tr> 

<tr> 
<td width="30%"valign="top"><b>Circuit breaking</b></td> 
<td width="70%">A method to prevent errors in one microservice from cascading to other microservices.
</td> 
</tr> 

<tr> 
<td width="30%"valign="top"><b>Configuration Change</b></td> 
<td width="70%"> A trigger that causes a new build to run when a new 
BuildConfig resource is created. </td> </tr>

<tr> 
<td width="30%"valign="top"><b>Control Plane</b></td> 
<td width="70%">The control plane takes the desired configuration and its view of the services and dynamically programs and updates the proxy servers as the environment changes. </td> </tr>

<tr> 
<td width="30%"valign="top"><b>Custom build strategy</b></td> 
<td width="70%"> Requires you to define and create your own builder image. </td> </tr>

<tr> 
<td width="30%"valign="top"><b>Custom builder images</b></td> 
<td width="70%"> Are regular Docker images that contain the logic needed to transform the inputs into the expected output. </td> </tr>

<tr> 
<td width="30%"valign="top"><b>CRDs</b></td> 
<td width="70%"> Custom code that defines a resource to add to your Kubernetes API server without building a complete custom server.
</td> 
</tr>

<tr> 
<td width="30%"valign="top"><b>Custom controllers</b></td> 
<td width="70%"> Reconcile the custom resources (CRDs) actual state with its desired state.
</td> 
</tr> 

<tr> 
<td width="30%"valign="top"><b>Data plane</b></td> 
<td width="70%">Communication between services is handled by the data plane. If a service mesh is absent, the network cannot identify the type of traffic that flows, the source, and the destination and make any necessary decisions.
</td> 
</tr> 

<tr> 
<td width="30%"valign="top"><b>Enforceability (Control)</b></td> 
<td width="70%"> Istio provides control by enforcing policies across an entire fleet and ensures resources are fairly distributed among consumers.
</td> 
</tr> 

<tr> 
<td width="30%"valign="top"><b>Envoy proxy</b></td> 
<td width="70%">All network traffic is subject to or intercepted by a proxy, called Envoy, used by the service mesh and allows many features depending on the configuration.
</td> 
</tr> 

<tr> 
<td width="30%"valign="top"><b>Human operators</b></td> 
<td width="70%"> Understand the systems they control. They know how to deploy services and how to recognize and fix problems. 
</td> 
</tr> 

<tr> 
<td width="30%"valign="top"><b>Image Change</b></td> 
<td width="70%"> A trigger to rebuild a containerized application when a new or updated version of an image is available. For example, if an application is built using a Node.js base image, that image will be updated as security fixes are released and other updates occur.   
</td> </tr>

<tr> 
<td width="30%"valign="top"><b>ImageStream</b></td> 
<td width="70%"> An abstraction for referencing container images within OpenShift. Each image contains an ID, or digest, that identifies it. ImageStreams do not contain image data but rather are pointers to image digests.  </td> </tr> 

<tr> 
<td width="30%"valign="top"><b>ImageStream Tag</b></td> 
<td width="70%">An identity to the pointer in an ImageStream that points to a certain image in a registry.  </td> </tr> 

<tr> 
<td width="30%"valign="top"><b>Istio</b></td> 
<td width="70%">A platform-independent and popular service mesh platform, often used with Kubernetes. It intelligently controls the flow of traffic and API calls between services, conducts a range of tests and reduces the complexity of managing network services. Istio secures services through authentication, authorization, and encryption. Istio provides control by defining policies that can be enforced across an entire fleet. With Istio, you can observe traffic flow in your mesh so you can trace call flows, dependencies, and you can view service communication metrics such as latency, traffic, errors and saturation. 
</td> </tr> 

<tr> 
<td width="30%"valign="top"><b>Man-in-the-middle attacks</b></td> 
<td width="70%">A man-in-the-middle (MiTM) attack is a type of cyber-attack where the attacker secretly intercepts and relays messages between two parties who believe they are communicating directly with each other. The attack is a type of eavesdropping in which the attacker intercepts and then controls the entire conversation. </td> </tr> 

<tr> 
<td width="30%"valign="top"><b>Observability</b></td> 
<td width="70%">Helps to observe the traffic flow in your mesh, trace call flows and dependencies, and view metrics such as latency and errors. </td> </tr> 

<tr> 
<td width="30%"valign="top"><b>OpenShift</b></td> 
<td width="70%"> A hybrid cloud, enterprise Kubernetes application. </td> </tr> 

<tr> 
<td width="30%"valign="top"><b>OpenShift CI/CD process </b></td> 
<td width="70%">Automatically merges new code changes to the repository, builds, tests, approves, and deploys a new version to different environments. </td> </tr> 

<tr> 
<td width="30%"valign="top"><b>Operators</b></td> 
<td width="70%">Automate cluster tasks and act as a custom controller to extend the Kubernetes API. </td> </tr> 

<tr> <td width="30%" valign="top"><b>Operator Framework</b></td> 
<td width="70%"> Is a family of tools and capabilities to deliver an efficient customer experience. It is not just about writing code; what is also critical is testing, delivery, and updating Operators. 
</td> </tr> 

<tr> <td width="30%" valign="top"><b>OperatorHub</b></td> 
<td width="70%"> Web console lets cluster administrators find Operators to install on their cluster. It provides many different types of Operators available, including Red Hat Operators, Certified Operators from independent service vendors partnered with Red Hat, Community Operators from the open-source community but not officially supported by Red Hat, and custom Operators defined by users.
</td> </tr> 
<tr> <td width="30%" valign="top"><b>Operator Lifecycle Manager</b></td> 
<td width="70%">(or OLM) Controls the install, upgrade, and role-based access control (or RBAC) of Operators in a cluster.  
</td> </tr> 

<tr> <td width="30%" valign="top"><b>Operator maturity model</b></td> 
<td width="70%"> Defines the phases of maturity for general day two Operations activities and ranges from Basic Install to Auto Pilot. 
</td> </tr> 

<tr> <td width="30%" valign="top"><b>Operator Pattern</b></td> 
<td width="70%"> A system design that links a Controller to one or more custom resources. 
</td> </tr> 

<tr> <td width="30%" valign="top"><b>Operator Registry</b></td> 
<td width="70%">Stores CRDs, cluster service versions (CSVs), and Operator metadata for packages and channels. It runs in Kubernetes or OpenShift clusters to provide the Operator catalog data to OLM.
</td> </tr> 

<tr> <td width="30%" valign="top"><b>Operator SDK </b></td> 
<td width="70%">(which includes Helm, Go, and Ansible) Helps authors build, test, and package their Operators without requiring knowledge of Kubernetes API complexities.
</td> </tr> 

<tr> <td width="30%" valign="top"><b>postCommit</b></td> 
<td width="70%"> Section defines an optional build hook. 
</td> </tr> 

<tr> <td width="30%" valign="top"><b>Retries</b></td> 
<td width="70%"> A method to prevent errors in one microservice from cascading to other microservices.
</td> </tr> 

<tr> <td width="30%" valign="top"><b>runPolicy</b></td> 
<td width="70%">Field controls how builds created from a build configuration need to run. Values include the default Serial (sequentially) and simultaneously. 
</td> </tr> 

<tr> <td width="30%" valign="top"><b>Service Broker</b></td> 
<td width="70%"> Provides a short-running process that cannot perform the consecutive day’s operations such as upgrades, failover, or scaling.
</td> </tr> 

<tr> <td width="30%" valign="top"><b>Service Mesh</b></td> 
<td width="70%"> A dedicated layer for making service-to-service 
communication secure and reliable. It provides traffic 
management to control the flow of traffic between 
services, security to encrypt traffic between services, 
and observability of service behavior; so, you can 
troubleshoot and optimize applications.
</td> </tr>

<tr> <td width="30%" valign="top"><b>Software operators</b></td> 
<td width="70%">Try to capture the knowledge of human operators and automate the same processes. 
</td> </tr>

<tr> 
<td width="30%"valign="top"><b>Source-to-Image</b></td> 
<td width="70%"> A tool for building reproducible container
images. Also abbreviated S2i, it injects application 
source code into a container image to produce a ready-to-run image. </td> </tr> 

<tr> 
<td width="30%"valign="top"><b>Source strategy</b></td> 
<td width="70%"> Section shows the strategy used to execute the build, such as a Source, Docker, or Custom strategy. </td> </tr> 

<tr> 
<td width="30%"valign="top"><b>Source type</b></td> 
<td width="70%"> Determines the primary input like a Git repository, an inline Dockerfile, or binary payloads. </td> </tr> 

<tr> <td width="30%" valign="top"><b>Webhook</b></td> 
<td width="70%"> A trigger that sends a request to an OpenShift Container Platform API endpoint. Often this will be a GitHub webhook, though it can also be a generic webhook. If a GitHub webhook is utilized, GitHub can send the request to OpenShift when there is a new commit on a certain branch, or a pull request is merged, or under many more circumstances. Webhooks are a great way to automate development flows so that builds can occur automatically as new code is developed.
</td> </tr>
</table>

## <h3 align="center"> © IBM Corporation 2022. All rights reserved. <h3/>
