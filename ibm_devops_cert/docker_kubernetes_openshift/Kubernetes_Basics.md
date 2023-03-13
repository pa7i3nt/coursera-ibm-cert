---
markdown-version: v1
tool-type: instructional-lab
branch: lab-2818-instruction
version-history-start-date: '2022-12-15T12:23:17Z'
---
<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/cc201/images/IDSN-logo.png" width="200" alt="cognitiveclass.ai logo">

##

<div align="center">
<b>Glossary: Kubernetes Basics</b>
</div>
<br>

<table>
<tr>
<th width="30%">Term</th width="70%"><th>Definition</th>
</tr>

<tr>
<td width="30%"><b>Automated bin packing </b></td>
<td width="70%">Increases resource utilization and cost savings using a mix of critical and best-effort workloads.
</tr>

<tr>
<td width="30%"><b>Batch execution</b></td>
<td width="70%">Manages batch and continuous integration workloads and automatically replaces failed containers, if configured.
</tr>

<tr>
<td width="30%"><b>Cloud Controller Manager</b></td>
<td width="70%">A Kubernetes control plane component that embeds cloud-specific control logic. The cloud controller manager lets you link your cluster into your cloud provider's API, and separates out the components that interact with that cloud platform from components that only interact with your cluster.
</tr>

<tr>
<td width="30%"><b>Cluster</b></td>
<td width="70%">A set of worker machines, called nodes, that run containerized applications. Every cluster has at least one worker node.
</tr>

<tr>
<td width="30%"valign="top"><b>Container 
Orchestration
</b></td>
<td width="70%">
Container orchestration is a process that automates the container lifecycle of containerized applications. 
</td>
</tr>

<tr>
<td width="30%"valign="top"><b>Container Runtime</b></td>
<td width="70%">
The container runtime is the software that is responsible for running containers.
</td>
</tr>

<tr>
<td width="30%"valign="top"><b>Control Loop</b></td>
<td width="70%">
A non-terminating loop that regulates the state of a 
system. A thermostat is an example of a control loop.
</td>
</tr>

<tr>
<td width="30%"valign="top"><b>Control plane</b></td>
<td width="70%">
The container orchestration layer that exposes the API and interfaces to define, deploy, and manage the lifecycle of containers.
</td>
</tr>

<tr>
<td width="30%"valign="top"><b>Controller</b></td>
<td width="70%">
In Kubernetes, controllers are control loops that watch the state of your cluster, then make or request changes where needed. Each controller tries to move the current cluster state closer to the desired state.
</td>
</tr>

<tr>
<td width="30%"valign="top"><b>Data (Worker) Plane</b></td>
<td width="70%">
The layer that provides capacity such as CPU, memory, network, and storage so that the containers can run and connect to a network.
</td>
</tr>

<tr>
<td width="30%"valign="top"><b>DaemonSet</b></td>
<td width="70%">
Ensures a copy of a Pod is running across a set of nodes in a cluster.
</td>
</tr>

<tr>
<td width="30%"valign="top"><b>Declarative 
Management
</b></td>
<td width="70%">
A desired state that can be expressed (for example, the 
number of replicas of a specific application),and 
Kubernetes will actively work to ensure that the 
observed state matches the desired state.

</td>
</tr>

<tr>
<td width="30%"valign="top"><b>Deployment</b></td>
<td width="70%">
An object that provides updates for both Pods and 
ReplicaSets. Deployments run multiple replicas of an 
application by creating ReplicaSets and offering 
additional management capabilities on top of those 
ReplicaSets. In addition, deployments are suitable for 
stateless applications.
</td>
</tr>

<tr>
<td width="30%"valign="top"><b>Designed for extensibility</b></td>
<td width="70%">
Adds features to your cluster without adding or modifying source code.
</td>
</tr>

<tr>
<td width="30%"valign="top"><b>Docker Swarm</b></td>
<td width="70%">
automates the deployment of containerized applications but was designed specifically to work with Docker Engine and other Docker tools making it a popular choice for teams already working in Docker environments. 
</td>
</tr>

<tr>
<td width="30%"valign="top"><b>Ecosystem</b></td>
<td width="70%">
A composition of services, support and tools that are widely available. The Kubernetes ecosystem is a large, rapidly growing ecosystem where its services, support, and tools are widely available.  
</td>
</tr>

<tr>
<td width="30%"valign="top"><b>etcd</b></td>
<td width="70%">
A highly available key value store that contains all the cluster data. For any deployment, the deployment configuration is stored in etcd. It is the source of truth for the state in a Kubernetes cluster, and the system works to bring the cluster state into line with what is stored in etcd. 
</td>
</tr>

<tr>
<td width="30%"valign="top"><b>Eviction</b></td>
<td width="70%">
Process of terminating one or more Pods on Nodes.
</td>
</tr>

<tr>
<td width="30%"valign="top"><b>Imperative commands</b></td>
<td width="70%">
Create, update, and delete live objects directly.
</td>
</tr>

<tr>
<td width="30%" valign="top"><b>Imperative Management </b></td>
<td width="70%">
Defining steps and actions to get to a desired state.

</td>
</tr>

<tr>
<td width="30%" valign="top"><b>Ingress</b></td>
<td width="70%">
An API object that manages external access to the services in a cluster, typically HTTP.
</td>
</tr>

<tr>
<td width="30%" valign="top"><b>IPv4/IPv6 dual stack</b></td>
<td width="70%">
Assigns both IPv4 and IPv6 addresses to Pods and Services.
</td>
</tr>

<tr>
<td width="30%" valign="top"><b>Job</b></td>
<td width="70%">
A finite or batch task that runs to completion.
</td>
</tr>

<tr>
<td width="30%" valign="top"><b>Kubectl</b></td>
<td width="70%">
Also known as kubectl Command line tool for communicating with a Kubernetes cluster's control plane, using the Kubernetes API.
</td>
</tr>

<tr>
<td width="30%" valign="top"><b>Kubelet</b></td>
<td width="70%">
The kubelet is the primary "node agent" that runs on each node. The kubelet takes a set of PodSpecs (a YAML or JSON object that describes a pod) provided primarily through the apiserver and ensures that the containers described in those PodSpecs are running and healthy. The kubelet doesn't manage containers which were not created by Kubernetes.
</td>
</tr>

<tr>
<td width="30%" valign="top"><b>Kubernetes</b></td>
<td width="70%">
is the de facto open-source platform standard for container orchestration. It was developed by Google and is maintained by the Cloud Native Computing Foundation (CNCF). Kubernetes automates container management tasks, like deployment, storage provisioning, load balancing and scaling, service discovery, and fixing failed containers. Its open-source toolset and wide array of functionalities are very attractive to leading cloud providers, who both support it, and in some cases, also offer fully managed Kubernetes services.
</td>
</tr>

<tr>
<td width="30%" valign="top"><b>Kubernetes API</b></td>
<td width="70%">
The application that serves Kubernetes functionality through a RESTful interface and stores the state of the cluster.
</td>
</tr>

<tr>
<td width="30%" valign="top"><b>Kubernetes API Server</b></td>
<td width="70%">
The Kubernetes API server validates and configures data for the api objects which include pods, services, replication controllers, and others. The API Server services REST operations and provides the frontend to the cluster's shared state through which all other components interact.
</td>
</tr>

<tr>
<td width="30%" valign="top"><b>Kubernetes Controller 
Manager</b></td>
<td width="70%">
Runs all the controller processes that monitor the cluster state and ensures that the actual state of a cluster matches the desired state. Examples of controllers that ship with Kubernetes are the replication controller, endpoints controller, namespace controller, and service accounts controller.
</td>
</tr>

<tr>
<td width="30%" valign="top"><b>Kubernetes Cloud Controller Manager</b></td>
<td width="70%">
A Kubernetes control plane component that embeds cloud-specific control logic. The cloud controller manager lets you link your cluster into your cloud provider's API, and separates out the components that interact with that cloud platform from components that only interact with your cluster.
</td>
</tr>

<tr>
<td width="30%" valign="top"><b>Kubernetes Proxy </b></td>
<td width="70%">
A network proxy that runs on each node in a cluster. This proxy maintains network rules that allow communication to Pods running on nodes—in other words, communication to workloads running on the cluster. The user must create a service with the apiserver API to configure the proxy.
</td>
</tr>

<tr>
<td width="30%" valign="top"><b>kube-scheduler</b></td>
<td width="70%">
Control plane component that watches for newly created Pods with no assigned node, and selects a node for them to run on.
</td>
</tr>

<tr>
<td width="30%" valign="top"><b>Label Selector </b></td>
<td width="70%">
Allows users to filter a list of resources based on labels.
</td>
</tr>

<tr>
<td width="30%" valign="top"><b>Labels</b></td>
<td width="70%">
Tags objects with identifying attributes that are meaningful and relevant to users.
</td>
</tr>

<tr>
<td width="30%" valign="top"><b>Load balancing</b></td>
<td width="70%">
Balances traffic across Pods for better performance and high availability.
</td>
</tr>

<tr>
<td width="30%" valign="top"><b>Marathon</b></td>
<td width="70%">
is an Apache Mesos framework. Apache Mesos is an open-source cluster manager developed by UC Berkeley. It lets users scale container infrastructure through the automaton of most management and monitoring tasks.
</td>
</tr>

<tr>
<td width="30%" valign="top"><b>Namespace</b></td>
<td width="70%">
An abstraction used by Kubernetes to support isolation of groups of resources within a single cluster. 
</td>
</tr>

<tr>
<td width="30%" valign="top"><b>Node</b></td>
<td width="70%">
The worker machine in a Kubernetes cluster. User 
applications are run on nodes. Nodes can be virtual or 
physical machines. Each node is managed by the control 
plane and is able to run Pods.
</td>
</tr>

<tr>
<td width="30%" valign="top"><b>Nomad</b></td>
<td width="70%">
(Hashicorp) is a free and open-source cluster management and scheduling tool that supports Docker and other applications on all major operating systems across all infrastructure, whether on-premises or in the cloud. This flexibility lets teams work with any type and level of workload.
</td>
</tr>

<tr>
<td width="30%" valign="top"><b>Object</b></td>
<td width="70%">
An entity in the Kubernetes system. The Kubernetes API uses these entities to represent the state of your cluster.
</td>
</tr>

<tr>
<td width="30%" valign="top"><b>Persistence</b></td>
<td width="70%">
Ensures that an object exists in the system, until the 
object is modified or removed.
</td>
</tr>

<tr>
<td width="30%" valign="top"><b>Preemption</b></td>
<td width="70%">
Logic in Kubernetes helps a pending Pod to find a suitable Node by evicting low priority Pods existing on that Node.
</td>
</tr>

<tr>
<td width="30%" valign="top"><b>Self-healing</b></td>
<td width="70%">
Restarts, replaces, reschedules, and kills failing or unresponsive containers.
</td>
</tr>

<tr>
<td width="30%" valign="top"><b>Service</b></td>
<td width="70%">
An abstract way to expose an application running on a set of Pods as a network service.
</td>
</tr>

<tr>
<td width="30%" valign="top"><b>Service Discovery</b></td>
<td width="70%">
Discovers Pods using their IP addresses or a single DNS name.
</td>
</tr>

<tr>
<td width="30%" valign="top"><b>StatefulSet</b></td>
<td width="70%">
Manages the deployment and scaling of a set of Pods, and provides guarantees about the ordering and uniqueness of these Pods.
</td>
</tr>

<tr>
<td width="30%" valign="top"><b>Storage</b></td>
<td width="70%">
A data store that supports persistent and temporary storage for Pods.
</td>
</tr>

<tr>
<td width="30%" valign="top"><b>Storage Orchestration</b></td>
<td width="70%">
Automatically mounts your chosen storage system whether from local storage, network storage, or public cloud.
</td>
</tr>

<tr>
<td width="30%" valign="top"><b>Pod</b></td>
<td width="70%">
The smallest and simplest Kubernetes object.  Represents a process running in a cluster; it also represents a single instance of an application running in a cluster. Usually, a Pod wraps a single container but, in some cases encapsulates multiple tightly coupled containers that share resources. 
</td>
</tr>

<tr>
<td width="30%" valign="top"><b>Proxy</b></td>
<td width="70%">
In computing, a proxy is a server that acts as an intermediary for a remote service. 
</td>
</tr>

<tr>
<td width="30%" valign="top"><b>ReplicaSet</b></td>
<td width="70%">
A ReplicaSet (aims to) maintain a set of replica Pods running at any given time.
</td>
</tr>

<tr>
<td width="30%" valign="top"><b>Workload</b></td>
<td width="70%">
A workload is an application running on Kubernetes.
</td>
</tr>
</table>

## <h3 align="center"> © IBM Corporation 2022. All rights reserved. <h3/>
