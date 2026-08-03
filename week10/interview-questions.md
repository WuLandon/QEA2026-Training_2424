# Interview Questions: Week 10 - AWS, DevOps

> **Quality Assurance Agent Output**
> 
> This question bank validates trainee retention of Week 10 concepts covering AWS Fundamentals, Docker & Containerization, DevOps Philosophy & Monitoring, and Jenkins CI/CD.
> 
> **Difficulty Distribution:** 70% Beginner | 25% Intermediate | 5% Advanced

---

## Beginner (Foundational)

### Q1: What are the three cloud service models, and what does each one mean?

**Keywords:** IaaS, PaaS, SaaS, Responsibility, Management

**Related notes:** [AWS Introduction — Cloud Service Models](2-tuesday/written/aws-introduction.md#cloud-service-models)

<details>
<summary>Click to Reveal Answer</summary>

The three cloud service models are:

1. **IaaS (Infrastructure as a Service):** You rent raw computing resources (virtual machines, storage, networking). You manage everything from the operating system up. AWS Examples: EC2, S3, VPC.

2. **PaaS (Platform as a Service):** The provider handles infrastructure, and you focus on your application. The platform manages servers, load balancing, and scaling automatically. AWS Examples: Elastic Beanstalk, RDS.

3. **SaaS (Software as a Service):** Fully managed applications accessed via web browser. You only manage your data and user access. Examples: Gmail, Salesforce, Microsoft 365.

</details>

---

### Q2: What is IAM in AWS, and what are its four core components?

**Keywords:** Identity, Access, Users, Groups, Roles, Policies

**Related notes:** [AWS Introduction — IAM Basics](2-tuesday/written/aws-introduction.md#iam-basics)

<details>
<summary>Click to Reveal Answer</summary>

**IAM (Identity and Access Management)** controls who can access what in your AWS account.

The four core components are:

1. **Users:** Individual identities for people or applications
2. **Groups:** Collections of users sharing the same permissions
3. **Roles:** Temporary credentials for services or cross-account access
4. **Policies:** JSON documents defining permissions (what actions are allowed/denied on which resources)

Best practices include: never using root account for daily tasks, enabling MFA, granting least privilege, and using groups to assign permissions.

</details>

---

### Q3: What is a Security Group in AWS?

**Keywords:** Virtual Firewall, Inbound, Outbound, Stateful, Instance-level

**Related notes:** [Security Groups — What is a Security Group?](2-tuesday/written/security-groups.md#what-is-a-security-group), [Key Characteristics](2-tuesday/written/security-groups.md#key-characteristics), and [Inbound vs Outbound Rules](2-tuesday/written/security-groups.md#inbound-vs-outbound-rules)

<details>
<summary>Click to Reveal Answer</summary>

A **Security Group** acts as a virtual firewall for AWS resources, controlling inbound and outbound traffic at the instance level.

Key characteristics:
- **Default Deny:** All inbound traffic is denied unless explicitly allowed
- **Stateful:** If traffic is allowed in one direction, the response traffic is automatically allowed
- **Allow Rules Only:** You cannot create deny rules—only allow rules
- **Instance Level:** Applied to individual EC2 instances or other resources
- **Multiple SGs:** An instance can have multiple security groups attached

Security groups control which ports are open and from which IP addresses traffic can originate.

</details>

---

### Q4: What is the difference between Docker containers and virtual machines?

**Keywords:** Kernel, Isolation, Overhead, Startup, Portability

**Related notes:** [Docker Introduction — Containerization vs Virtualization](3-wednesday/written/docker-introduction.md#containerization-vs-virtualization)

<details>
<summary>Click to Reveal Answer</summary>

| Aspect | Virtual Machines | Containers |
|--------|------------------|------------|
| **Size** | GBs (includes full guest OS) | MBs (app + libraries only) |
| **Startup** | Minutes | Seconds |
| **Isolation** | Hardware-level via hypervisor | Process-level via container engine |
| **Kernel** | Each VM has its own kernel | Containers share the host OS kernel |
| **Density** | 10s per host | 100s per host |

Containers are more lightweight because they share the host operating system kernel, while VMs each include a complete guest operating system, resulting in more overhead.

</details>

---

### Q5: What is a Dockerfile and what are five essential instructions used in it?

**Keywords:** Build, Image, FROM, RUN, COPY, CMD, Layers

**Related notes:** [Dockerfiles — What is a Dockerfile?](3-wednesday/written/dockerfiles.md#what-is-a-dockerfile) and [Essential Dockerfile Instructions](3-wednesday/written/dockerfiles.md#essential-dockerfile-instructions)

<details>
<summary>Click to Reveal Answer</summary>

A **Dockerfile** is a text file containing instructions for building a Docker image. Each instruction creates a layer in the resulting image.

Five essential instructions:

1. **FROM:** Specifies the base image (required, must be first). Example: `FROM python:3.11`
2. **WORKDIR:** Sets the working directory inside the container. Example: `WORKDIR /app`
3. **COPY:** Copies files from the build context into the image. Example: `COPY . /app`
4. **RUN:** Executes a command during build (creates a layer). Example: `RUN pip install -r requirements.txt`
5. **CMD:** Specifies the default command to run when the container starts. Example: `CMD ["python", "app.py"]`

</details>

---

### Q6: What are Docker volumes and why are they important?

**Keywords:** Persistence, Data, Container Lifecycle, Named, Bind Mount

**Related notes:** [Docker Volumes — The Data Persistence Problem](3-wednesday/written/docker-volumes.md#the-data-persistence-problem), [Types of Docker Storage](3-wednesday/written/docker-volumes.md#types-of-docker-storage), and [Volume vs Bind Mount Comparison](3-wednesday/written/docker-volumes.md#volume-vs-bind-mount-comparison)

<details>
<summary>Click to Reveal Answer</summary>

**Docker volumes** provide persistent storage that exists outside the container lifecycle. When a container is removed, its filesystem is deleted—but data stored in volumes persists.

Three types of Docker storage:

1. **Named Volumes:** Docker-managed storage, best for production data
2. **Bind Mounts:** Map host filesystem directories into containers, best for development
3. **tmpfs:** Memory-only storage, data lost when container stops

Volumes are important because real applications need persistent data: databases store records, applications save uploads, and logs must survive container restarts.

</details>

---

### Q7: What is DevOps and what are its three main components?

**Keywords:** Culture, Practices, Tools, Collaboration, Automation

**Related notes:** [DevOps Introduction — What is DevOps?](4-thursday/written/devops-introduction.md#what-is-devops), [DevOps Culture](4-thursday/written/devops-introduction.md#devops-culture-breaking-down-silos), and [DevOps Core Practices](4-thursday/written/devops-introduction.md#devops-core-practices)

<details>
<summary>Click to Reveal Answer</summary>

**DevOps** is a set of practices, cultural philosophies, and tools that increases an organization's ability to deliver applications and services at high velocity.

The three main components are:

1. **Culture:** Shared responsibility, trust, blameless postmortems, continuous learning, breaking down silos between development and operations teams

2. **Practices:** Continuous Integration, Continuous Delivery/Deployment, Infrastructure as Code, Monitoring, Automation

3. **Tools:** Jenkins, Docker, Kubernetes, Prometheus, Grafana, Terraform, Git, Ansible

DevOps is NOT just automation or tools—culture is foundational. "You build it, you run it" represents the shared ownership philosophy.

</details>

---

### Q8: What is Prometheus and what type of monitoring does it provide?

**Keywords:** Metrics, Time-series, Pull-based, Scrape, PromQL

**Related notes:** [Prometheus Essentials — What is Prometheus?](4-thursday/written/prometheus-essentials.md#what-is-prometheus), [Prometheus Architecture](4-thursday/written/prometheus-essentials.md#prometheus-architecture), and [Pull-Based vs Push-Based Monitoring](4-thursday/written/prometheus-essentials.md#pull-based-vs-push-based-monitoring)

<details>
<summary>Click to Reveal Answer</summary>

**Prometheus** is an open-source systems monitoring and alerting toolkit that provides metrics-based monitoring. It's the industry standard for cloud-native environments.

Key characteristics:
- **Time-series database:** Stores metrics indexed by time with labels for dimensions
- **Pull-based collection:** Prometheus scrapes (pulls) metrics from targets via HTTP endpoints
- **Multi-dimensional data model:** Metrics identified by name plus key-value labels
- **PromQL:** Flexible query language for querying and aggregating metrics
- **Built-in alerting:** Can trigger alerts based on metric conditions

Prometheus is best for: application performance monitoring, infrastructure metrics, business metrics, and SLA/SLO monitoring.

</details>

---

### Q9: What is Grafana and how does it relate to Prometheus?

**Keywords:** Visualization, Dashboards, Data Source, Panels, Queries

**Related notes:** [Grafana Overview — What is Grafana?](4-thursday/written/grafana-overview.md#what-is-grafana), [Data Source Concept](4-thursday/written/grafana-overview.md#data-source-concept), and [Connecting a Prometheus Data Source](4-thursday/written/connecting-data-sources.md#adding-prometheus-data-source)

<details>
<summary>Click to Reveal Answer</summary>

**Grafana** is an open-source platform for monitoring and observability visualization. It transforms time-series data into meaningful dashboards.

Relationship with Prometheus:
- Prometheus collects and stores metrics
- Grafana visualizes those metrics through dashboards
- Grafana connects to Prometheus as a **data source** and queries it using PromQL

Key features:
- Multiple panel types (graphs, gauges, tables, heatmaps)
- Dashboard templating with variables
- Alerting and notifications
- Supports many data sources beyond Prometheus

Grafana doesn't store data—it queries external data sources like Prometheus, InfluxDB, Elasticsearch, and cloud providers.

</details>

---

### Q10: What is Jenkins and what is its primary purpose?

**Keywords:** CI/CD, Automation, Pipelines, Builds, Open-source

**Related notes:** [Introduction to Jenkins — What is Jenkins?](5-friday/written/jenkins-introduction.md#what-is-jenkins) and [Jenkins Architecture](5-friday/written/jenkins-introduction.md#jenkins-architecture)

<details>
<summary>Click to Reveal Answer</summary>

**Jenkins** is an open-source automation server that enables Continuous Integration and Continuous Delivery (CI/CD). It's the most widely adopted CI/CD tool in the industry.

Primary purpose and capabilities:
- **Build automation:** Compile code, create artifacts
- **Test automation:** Run unit, integration, and E2E tests
- **Deployment:** Deploy applications to any environment
- **Workflow orchestration:** Pipeline as code via Jenkinsfile
- **Scheduled tasks:** Cron-like job scheduling

Jenkins automates the path from code commit to production deployment, orchestrating the entire software delivery pipeline. It has 1500+ plugins for integration with virtually any tool.

</details>

---

### Q11: What is a Jenkinsfile and why is "Pipeline as Code" important?

**Keywords:** Version Control, Repository, Declarative, Stages, Reproducible

**Related notes:** [Jenkinsfile and Pipeline Syntax — Pipeline as Code](5-friday/written/jenkinsfile.md#pipeline-as-code) and [Pipeline Structure](5-friday/written/jenkinsfile.md#pipeline-structure)

<details>
<summary>Click to Reveal Answer</summary>

A **Jenkinsfile** is a text file that defines a Jenkins pipeline using code syntax. It's stored in the application's source code repository alongside the application code.

**Pipeline as Code** is important because:
- **Version controlled:** Pipeline changes are tracked in Git with full history
- **Code reviewed:** Pipeline modifications go through pull request reviews
- **Reproducible:** Anyone can recreate the pipeline from the Jenkinsfile
- **Branch-specific:** Different branches can have different pipeline configurations
- **Self-documenting:** The pipeline configuration serves as documentation

This contrasts with traditional "click-through" UI configuration, which is hard to replicate, audit, or version control.

</details>

---

## Intermediate (Application)

### Q12: Your test cannot connect to an RDS database from an EC2 instance. What AWS component should you check first, and how would you fix it?

**Hint:** Think about network traffic rules between AWS resources.

**Keywords:** Security Group, Inbound Rules, Port, Source

**Related notes:** [Security Groups — Security Group References](2-tuesday/written/security-groups.md#security-group-references), [Add Inbound Rules](2-tuesday/written/security-groups.md#add-inbound-rules), and [RDS Security](2-tuesday/written/rds-introduction.md#rds-security)

<details>
<summary>Click to Reveal Answer</summary>

You should check the **Security Group** attached to the RDS database instance.

Troubleshooting steps:

1. **Verify the RDS security group has an inbound rule** allowing traffic on the database port (e.g., 3306 for MySQL, 5432 for PostgreSQL)

2. **Check the source of the rule** - it should either:
   - Reference the EC2 instance's security group (recommended): `sg-webapp123`
   - Include the EC2 instance's IP address or subnet CIDR

3. **Create/modify the rule** if missing:
   ```
   Type: MySQL/Aurora (or PostgreSQL, etc.)
   Port: 3306 (or 5432, etc.)
   Source: sg-ec2-instance-security-group
   ```

Using security group references (instead of IP addresses) is a best practice because it automatically allows access from any instance using that security group, even when IPs change or Auto Scaling adds instances.

</details>

---

### Q13: You need to reduce the size of your Docker image significantly. What technique should you use and how does it work?

**Hint:** Consider separating build dependencies from runtime.

**Keywords:** Multi-stage, Build, Runtime, Layers, COPY --from

**Related notes:** [Multi-Stage Dockerfiles — Multi-Stage Build Solution](3-wednesday/written/multi-stage-dockerfiles.md#multi-stage-build-solution), [How Multi-Stage Builds Work](3-wednesday/written/multi-stage-dockerfiles.md#how-multi-stage-builds-work), and [Java Multi-Stage Build](3-wednesday/written/multi-stage-dockerfiles.md#java-multi-stage-build)

<details>
<summary>Click to Reveal Answer</summary>

Use **multi-stage Docker builds** to significantly reduce image size.

How it works:

1. **Build stage:** Use a full image with build tools (compilers, package managers, etc.) to compile/build the application

2. **Runtime stage:** Use a minimal base image and copy only the compiled artifacts from the build stage

Example:
```dockerfile
# Build stage
FROM maven:3.8-jdk-17 AS build
WORKDIR /app
COPY . .
RUN mvn package

# Runtime stage
FROM eclipse-temurin:17-jre-alpine
COPY --from=build /app/target/*.jar app.jar
CMD ["java", "-jar", "app.jar"]
```

Benefits:
- Build tools (Maven, npm, compilers) are NOT in the final image
- Final image contains only the runtime and application
- Can reduce image size from 1GB+ to under 100MB
- Smaller attack surface for security

</details>

---

### Q14: A deployment went out and now error rates are spiking. Using Prometheus and Grafana, how would you investigate and what metrics would you look at?

**Hint:** Consider the "Four Golden Signals" of monitoring.

**Keywords:** Error Rate, Latency, Traffic, rate(), Dashboard

**Related notes:** [Common Metrics — The Four Golden Signals](4-thursday/written/common-metrics.md#the-four-golden-signals), [Four Golden Signals Queries](4-thursday/written/common-metrics.md#four-golden-signals-queries), [PromQL Error Rate Calculations](4-thursday/written/querying-metrics.md#error-rate-calculations), and [Grafana Dashboard Anatomy](4-thursday/written/dashboards.md#dashboard-anatomy)

<details>
<summary>Click to Reveal Answer</summary>

Investigation approach using the monitoring stack:

**1. Check Error Rate:**
```promql
# Error rate as percentage
sum(rate(http_requests_total{status=~"5.."}[5m])) / sum(rate(http_requests_total[5m])) * 100
```

**2. Compare Before/After Deployment:**
- Use Grafana's time range selector to compare current metrics vs before deployment
- Add annotations to mark deployment times

**3. Check Latency (Response Time):**
```promql
# 95th percentile latency
histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m]))
```

**4. Check Traffic Volume:**
```promql
# Request rate
sum(rate(http_requests_total[5m])) by (endpoint)
```

**5. Check Resource Saturation:**
- CPU usage: `node_cpu_seconds_total`
- Memory usage: `node_memory_usage_bytes`

**6. Filter by Label to Isolate:**
```promql
# Errors for specific endpoint
rate(http_requests_total{status=~"5..", endpoint="/api/checkout"}[5m])
```

These align with the **Four Golden Signals**: Latency, Traffic, Errors, and Saturation.

</details>

---

### Q15: Write a basic Jenkinsfile that has three stages: Build, Test, and Deploy. The Deploy stage should only run on the main branch.

**Hint:** Use the `when` directive for conditional execution.

**Keywords:** pipeline, stages, steps, when, branch

**Related notes:** [Jenkinsfile — Basic Declarative Pipeline](5-friday/written/jenkinsfile.md#basic-declarative-pipeline), [Pipeline Stage Structure](5-friday/written/jenkins-pipeline-stages.md#stage-structure), and [Conditional Stages (`when`)](5-friday/written/jenkins-pipeline-stages.md#conditional-stages-when)

<details>
<summary>Click to Reveal Answer</summary>

```groovy
pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                echo 'Building application...'
                sh 'mvn clean compile'
            }
        }
        
        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'mvn test'
            }
            post {
                always {
                    junit 'target/surefire-reports/*.xml'
                }
            }
        }
        
        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                echo 'Deploying to production...'
                sh './deploy.sh'
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
```

Key elements:
- **pipeline {}:** Required wrapper for declarative syntax
- **agent any:** Run on any available Jenkins agent
- **stages {}:** Contains all stage definitions
- **when { branch 'main' }:** Conditional—Deploy only runs on main branch
- **post {}:** Actions that run after stages complete (success/failure handling)

</details>

---

## Advanced (Deep Dive)

### Q16: You're designing a CI/CD pipeline that builds a Docker image, runs tests, and deploys to AWS. Explain the complete flow including security considerations, and describe how you would handle secrets like AWS credentials and Docker registry passwords.

**Keywords:** Credentials, Pipeline, Security Groups, IAM Roles, Jenkins Credentials, Environment Variables

**Related notes:** [CI/CD Pipeline Stages](4-thursday/written/continuous-integration-delivery-deployment.md#cicd-pipeline-stages), [Complete Jenkins CI/CD Pipeline](5-friday/written/jenkinsfile.md#complete-cicd-pipeline), [Using Jenkins Credentials in Builds](5-friday/written/jenkins-credentials.md#using-credentials-in-builds), [Security Group Best Practices](2-tuesday/written/security-groups.md#security-group-best-practices), and [Container Security Considerations](3-wednesday/written/containerization.md#container-security-considerations)

<details>
<summary>Click to Reveal Answer</summary>

**Complete CI/CD Pipeline Design:**

**1. Pipeline Stages:**
```
Checkout → Build → Unit Tests → Build Docker Image → 
Push to Registry → Deploy to Staging → Integration Tests → 
Deploy to Production (with approval)
```

**2. Secret Management Approach:**

**For Jenkins:**
- Use **Jenkins Credentials** store (never hardcode secrets)
- Access via `withCredentials()` block or `credentials()` helper
- Secrets are masked in console output

```groovy
withCredentials([usernamePassword(
    credentialsId: 'docker-hub',
    usernameVariable: 'DOCKER_USER',
    passwordVariable: 'DOCKER_PASS'
)]) {
    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
}
```

**For AWS:**
- **Option 1 (Best):** Use **IAM Roles** attached to Jenkins agent EC2 instance—no credentials needed
- **Option 2:** Store AWS Access Key/Secret in Jenkins Credentials, inject as environment variables
- Never store credentials in Jenkinsfile or repository

**3. Security Considerations:**

**Network Security:**
- Jenkins agents in private subnet
- Security groups restricting access to Jenkins master
- RDS in private subnet, accessible only from application security group

**Credential Security:**
- Rotate credentials regularly
- Use IAM roles over access keys where possible
- Enable MFA on AWS accounts
- Limit credential scope (least privilege)

**Docker Security:**
- Scan images for vulnerabilities before pushing
- Use specific image tags (not `latest`)
- Run containers as non-root user
- Sign images if using private registry

**4. Infrastructure Security:**
- Enable encryption at rest (EBS, RDS, S3)
- Enable encryption in transit (HTTPS, TLS)
- Use private ECR instead of public Docker Hub for sensitive images
- Implement security groups with principle of least privilege

**5. Audit and Compliance:**
- Enable CloudTrail for AWS API logging
- Enable Jenkins audit logging
- Use blameless postmortems for incidents
- Document all pipeline changes via version control

This design follows DevOps security best practices while maintaining automation and velocity.

</details>

---

## Question Coverage Matrix

| Topic | Question Numbers |
|-------|------------------|
| AWS Cloud Models & IAM | Q1, Q2 |
| AWS Security Groups | Q3, Q12 |
| Docker Fundamentals | Q4 |
| Dockerfiles | Q5, Q13 |
| Docker Volumes | Q6 |
| DevOps Philosophy | Q7 |
| Prometheus | Q8, Q14 |
| Grafana | Q9, Q14 |
| Jenkins | Q10, Q15 |
| Jenkinsfile | Q11, Q15 |
| End-to-End CI/CD | Q16 |

---

## Self-Assessment Guide

**Scoring:**
- **Beginner Questions (Q1-Q11):** 5 points each = 55 points
- **Intermediate Questions (Q12-Q15):** 10 points each = 40 points
- **Advanced Question (Q16):** 5 points = 5 points
- **Total:** 100 points

**Evaluation:**
- **90-100:** Excellent – Ready for technical interviews
- **75-89:** Good – Review weak areas
- **60-74:** Fair – Need more practice
- **Below 60:** Review Week 10 materials thoroughly

---

*Generated by Quality Assurance Agent for CTSQEA Training Program*

