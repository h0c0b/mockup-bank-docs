from diagrams import Cluster, Diagram, Edge
from diagrams.aws.management import OrganizationsAccount, OrganizationsOrganizationalUnit, Organizations
from diagrams.onprem.certificates import CertManager, LetsEncrypt
from diagrams.onprem.vcs import Github
from diagrams.onprem.gitops import ArgoCD
from diagrams.onprem.client import Users

with Diagram("AWS Accounts Layout", outformat=["jpg"], filename="../img/acc_arch"):
