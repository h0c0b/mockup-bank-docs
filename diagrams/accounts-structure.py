from diagrams import Cluster, Diagram, Edge
from diagrams.aws.management import OrganizationsAccount, OrganizationsOrganizationalUnit, Organizations
from diagrams.onprem.certificates import CertManager, LetsEncrypt
from diagrams.onprem.vcs import Github
from diagrams.onprem.gitops import ArgoCD
from diagrams.onprem.client import Users

with Diagram("AWS Accounts Architecture", outformat=["jpg", "png"]):
    org_root = Organizations ("MockUp Org")
    ou_infra = OrganizationsOrganizationalUnit("Infra")
    ou_security = OrganizationsOrganizationalUnit("Security")
    ou_prod = OrganizationsOrganizationalUnit ("Prod")
    master_acc = OrganizationsAccount ("root")
    deploy_acc = OrganizationsAccount ("Deployment account")
    sec_acc = OrganizationsAccount ("Security account")
    log_acc = OrganizationsAccount ("Log Archive")
    org_root - master_acc
    org_root - ou_infra 
    org_root - ou_security 
    org_root - ou_prod

    ou_infra - deploy_acc
    ou_security - sec_acc
    ou_security - log_acc
    