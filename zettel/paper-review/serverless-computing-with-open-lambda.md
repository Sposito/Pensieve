#paper #OS
# Serverless Computing with OpenLambda
## Introduction
OpenLambda is a joint open-source effort to investigate and push forward serverless computation. In this article, \cite{hendrickson2016serverless} the authors discuss the benefits of current serverless computation solutions like AWS lambdas compared to containerised applications. It explores its shortcomings to propose areas where open lambda could further advance the field.

## Summary
After the theme introductions, the authors explore what we currently have in serverless computation with Amazon's Aws Lambda before discussing the technology's motivations. The next topic will be an overview of OpenLambda. It continues then on investigations agenda, passing by: Workloads analysis and executing engines, some pondering on interpreted languages, package management, sessions maintenance, databases and data aggregations, load balancers and costs control. Finally, it does conclude just before comparing previous monolithic architectures breakdowns.

## Analysis
Containers are poor fitting to microservices-based applications, serverless applications as the ones hosted in AWS Lambda are shown in the article to outperform containers for that kind of tasks because they automatically scale in response to load increases. OpenLambda is the base where researchers can evaluate new approaches in serverless computing.

## Conclusion
Serverless computing is far more elastic compared to virtualisation and even containers. It imposes new challenges with databases, schedulers and even local development. OpenLambda is a great tool for both research and cloud devs use for deployment

```
@inproceedings{hendrickson2016serverless,
  title={Serverless Computation with $\{$OpenLambda$\}$},
  author={Hendrickson, Scott and Sturdevant, Stephen and Harter, Tyler and Venkataramani, Venkateshwaran and Arpaci-Dusseau, Andrea C and Arpaci-Dusseau, Remzi H},
  booktitle={8th USENIX Workshop on Hot Topics in Cloud Computing (HotCloud 16)},
  year={2016}
}

```

