# Google Cloud Platform - Storage Architecture

## Requirement

Customer documents require different visibility levels.

## Bucket Layout

journeybuddy-documents/
│
├── public/
│   └── assets/
│
└── private/
    └── customer-documents/

## Access Model

Public assets:
- Can be read publicly.
- Should not be writable publicly.

Private documents:
- Require authentication.
- Access should follow least privilege.
- Administrative operations should use appropriate IAM roles.

## Recommended IAM Design

Public users:
- Object Viewer on public assets where appropriate.

Application service account:
- Access only to the required bucket objects.

Administrators:
- Storage administration permissions through an administrator role.

## Security Principle

Never make the entire bucket public merely to expose a small set of public assets.
Use IAM and application-level authorization to protect private customer documents.
