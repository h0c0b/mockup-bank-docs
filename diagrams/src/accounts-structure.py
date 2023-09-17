from diagrams import Diagram
from diagrams.aws.management import OrganizationsAccount, OrganizationsOrganizationalUnit, Organizations

graph_attr = {
    "splines": "spline",
}

with Diagram("AWS Accounts Layout", outformat=["jpg"], filename="../img/acc_arch", direction='LR'):
    org_root = Organizations ("MockUpBank Org")
    ou_infra = OrganizationsOrganizationalUnit("Infra OU")
    ou_security = OrganizationsOrganizationalUnit("Security OU")
    ou_prod = OrganizationsOrganizationalUnit ("Prod OU")
    ou_sandbox = OrganizationsOrganizationalUnit ("Sandbox OU")
    master_acc = OrganizationsAccount ("root")
    deploy_acc = OrganizationsAccount ("Deployment account")
    sec_acc = OrganizationsAccount ("Security account")
    log_acc = OrganizationsAccount ("Log Archive")
    dev_acc = OrganizationsAccount ("Dev Acc")
    prod_acc = OrganizationsAccount ("Production")
    org_root - master_acc
    org_root - ou_infra 
    org_root - ou_security 
    org_root - ou_prod
    org_root - ou_sandbox

    ou_infra - deploy_acc
    ou_security - sec_acc
    ou_security - log_acc
    ou_sandbox - dev_acc
    ou_prod - prod_acc
    