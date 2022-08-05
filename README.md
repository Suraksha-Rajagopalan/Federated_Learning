<div align = "center">
<h1> Federated Learning</h1>
</div>
Federated learning is a machine learning technique that trains an algorithm across multiple decentralized edge devices or servers holding local data samples, without exchanging them.
A common example of the application of federated learning is mobile phones. 
Mobile phones collectively study a shared prediction model, while keeping the device's training data local Instead of uploading and storing it.


<h3>How is federated learning different from the traditional method of learning (also called distributed learning)</h3>

Distributed learning uses ```centralized data```. This means that the whole organization works from the same blueprint, avoiding discrepancies that easily arise from disparate data and different tools. In colloquial terms, a centralized database has all its data collected and located at a single area therefore the security of the database is high but this type of database heavily depends on ```network connectivity```. If the network is slow it takes longer time to connect to the database. This became the reason for the usage of a decentralized database which doesn’t have its data at a centralized area, instead it is ```distributed```. This feature of decentralized database helps to avoid network connectivity issue. A federated learning uses decentralized data.

<div align = "center">
<img scr="https://user-images.githubusercontent.com/91787553/183024050-389b13eb-5aeb-4fb2-8f98-917076efb710.png" width="600">
</div>

<h3>Advantages of federated learning</h3>
<li>Allows devices such as smartphones to learn a shared prediction model collaboratively while maintaining the training data on the computer rather than uploading and storing it on a central server.</li>
<li>Moves model teaching to the edge, including gadgets like smartphones, laptops, IoT, and even "organizations" like hospitals that must work under stringent privacy regulations. It is a significant security advantage to keep personal data local.</li>
<li>Since prediction takes place on the system itself, real-time prediction is feasible. The time lag caused by sending raw data to a central server and then shipping the results back to the system is reduced by FL.</li>
<li>The prediction method works even though there is no internet connection because the models are stored on the device.</li>
<li>The amount of hardware equipment available is reduced.</li>


<h3>Challenges faced by FL </h3>
<li>Federated networks potentially include a massive number of devices (for example, millions of smartphones), and communication in the network can be slower than local computation by many orders of magnitude.</li>
<li>The storage, computational, and communication capabilities of the devices that are part of a federated network may differ significantly. Differences usually occur due to variability in hardware (CPU, memory), network connectivity (3G, 4G, 5G, wifi), and power supply (battery level).</li>
<li>Challenges arise when training federated models from data that is not identically distributed across devices, both in terms of modeling the data and in terms of analyzing the convergence behavior of associated training procedures.</li>
<li>Privacy concerns often motivate the need to keep raw data on each device local in federated settings. However, sharing other information such as model updates as part of the training process can also potentially reveal sensitive information, either to a third party or to the central server.</li>



<h3>How are the challenges been overcome by FL</h3>
<li><b>Communication-Efficiency</b></li>
Federated learning depends on communication-efficient methods that iteratively send small messages or model updates as part of the distributed training process instead of sending the entire dataset over the network.



There are two main goals to further reduce communication: 
<li>reducing the total number of communication rounds</li>
<li>reducing the size of transmitted messages at each round.</li>

<b>The following are general concepts that aim to achieve communication-efficient distributed learning methods:</b>
<li>Local updating methods allow for a variable number of local updates to be applied on each machine in parallel at each communication round. Thus, the goal of local updating methods is to reduce the total number of communication rounds.</li>
<li>Model compression schemes such as sparsification, subsampling, and quantization can significantly reduce the size of messages communicated at each update round.</li>
<li>Decentralized training. In the federated learning settings, a server connects with all remote devices. Decentralized topologies are an alternative when communication to the server becomes a bottleneck, especially when operating in low bandwidth or high latency networks.</li>


<li><b>Systems Heterogeneity</b></li>
federated learning methods have to be developed so that they can anticipate a low amount of participation, tolerate heterogeneous hardware, and are robust to dropped devices in the network.



<b>There are some key directions to handle systems heterogeneity:</b>
<li><b>Asynchronous communication</b> is used to parallelize iterative optimization algorithms. Asynchronous schemes are an attractive approach to mitigating stragglers in heterogeneous environments.</li>
<li><b>Active device sampling.</b> Typically, only a small subset of devices participate in each round of training. Therefore, an approach is to actively select participating devices at each round with the goal to aggregate as many device updates as possible within a pre-defined time window.</li>
<li><b>Fault tolerance.</b> A practical approach is to ignore device failure, which may lead to bias in the device sampling scheme if the failed devices have specific data characteristics. Coded computation is another option to tolerate device failures by introducing algorithmic redundancy.</li>
<li><b>Privacy Concerns</b> 
Recently methods aim to enhance the privacy of federated learning using secure multiparty computation (SMC) or differential privacy. However, those methods usually provide privacy at the cost of reduced model performance or system efficiency. Therefore, balancing these trade-offs is a considerable challenge in realizing private federated learning systems.

Recently, multiple privacy-preserving methods for machine learning have been researched. For example, the following three main strategies could be used for federated settings: Differential privacy to communicate noisy data sketches, homomorphic encryption to operate on encrypted data, and secure function evaluation or multiparty computation.
<li><b>Differential Privacy</b> is a popular privacy approach due to its strong information-theoretic guarantees, algorithmic simplicity, and comparably small systems overhead. A randomized mechanism is differentially private if the change of one input element will not result in too much difference in the output distribution. Therefore, it is not possible to draw conclusions about whether or not a specific sample is used in the learning process. Furthermore, there exists an inherent trade-off between differential privacy and model accuracy, as adding more noise results in greater privacy but may compromise accuracy significantly.</li>
<li><b>Homomorphic Encryption</b> can be used to secure the learning process by computing on encrypted data. However, it has currently been applied in limited settings, e.g., training linear models or involving only a few entities</li>
<li><b>Secure multiparty computation (SMC) or secure function evaluation (SFE)</b> are other options for performing privacy-preserving learning with sensitive datasets distributed across different data owners. Those protocols enable multiple parties to collaboratively compute an agreed-upon function without leaking raw input information from any party except for what can be inferred from the output. SMC is a lossless method and can retain the original accuracy with a very high privacy guarantee. To achieve even stronger privacy guarantees, SMC can be combined with differential privacy.</li>

Privacy in Federated Learning poses novel challenges to existing privacy-preserving algorithms. Most importantly, privacy-preserving methods have to offer rigorous privacy guarantees without overly compromising accuracy. Therefore, such methods have to be computationally cheap, communication-efficient, and tolerant to dropped devices.

Current implementations of privacy-preserving federated learning typically build around classical cryptographic protocols such as SMC and differential privacy. However, SMC techniques impose significant performance overheads, and their application to privacy-preserving deep learning remains an open problem.
</li>
