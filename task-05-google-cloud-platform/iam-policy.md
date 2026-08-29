# IAM Policy Design

## Roles

### Public Reader

Purpose:
Read public assets only.

Permission concept:
storage.objects.get

### Application Service Account

Purpose:
Read/write objects required by the application.

Access:
Only the required bucket and object paths.

### Administrator

Purpose:
Manage storage configuration and objects.

Access:
Administrative storage permissions.

## Principle

Apply least privilege: every identity receives only the permissions required to perform its job.
