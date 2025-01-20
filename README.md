# iota - CI/CD most simple project

The iota project comes from the initials _Inception Of Things App_.
It is a simple project that allows pushing new versions with an automatic
CI/CD pipeline for testing that has a helm chart for automatic releases
to k8s environments (with a special emphasis on ArgoCD). Nothing more than that!

## Setup

The setup can be done using `helm install` or by setting up the repository
in an ArgoCD instance.

As simple as that!

## Limitations

For simplicity reasons:
* serviceaccounts are not supported.

## Contributing

If for some extremely weird reason you believe a contribution can be helpful,
please open a PR. There is not much of a rule besides respecting the original
reason for its existance: a simple deployable application with automatic
image building, distribution, and releasing.
