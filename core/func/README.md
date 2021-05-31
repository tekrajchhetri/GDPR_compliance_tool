## System Requirements
- Linux systems
- faasd installation using bash
    - ```sh
            $ git clone https://github.com/openfaas/faasd --depth=1
            $ cd faasd
            $ ./hack/install.sh
       ```
- CLI installation
    - ```sh 
        $ curl -sSL https://cli.openfaas.com | sudo -E sh 
        ```
## Deployment
- [Deployment](https://docs.openfaas.com/deployment/)
- [Deployment guide for Kubernetes](https://docs.openfaas.com/deployment/kubernetes/)
-  ```sh 
        $ faas-cli up -f stack.yml 
   ```

  
## More Information
- [OpenFaaS](https://docs.openfaas.com/cli/install/)  
   

