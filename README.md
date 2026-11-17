# Linux Viikko 4

## Server Information

### Server A (Master)

OAMKlinux

IP: 195.148.23.158

Application:

http://195.148.23.158/viikko2/

### Server B (Replica)

Viikko4

IP: 195.148.30.94

Application:

http://195.148.30.94/viikko4/

---

## Snapshot

Server B was created from a snapshot of Server A in cPouta.

---

## Backup Solution

Website backups are created automatically on Server A and copied to Server B.

Backup script:

backup_www.sh

Backup destination:

/backups/website

Cron schedule:

0 * * * * /home/ubuntu/backup_www.sh

Stored versions:

- Latest backup
- Previous backup

---

## Restore Test

A backup archive was restored successfully to:

/home/ubuntu/restore_test

The restored files matched the original website content.

---

## Database Replication

MySQL replication was configured from OAMKlinux (master) to Viikko4 (replica).

Replication status:

- Replica_IO_Running: Yes
- Replica_SQL_Running: Yes

The replica server displays data from its own local replicated database.

---

## Read-Only Replica Page

The page available at:

http://195.148.30.94/viikko4/

Displays the replicated counter value.

Loading the page does not increase the counter value.

---

## Why Replication Is Not a Backup

Replication copies changes immediately from the master server.

If data is deleted or corrupted on the master server, the same change is replicated to the replica server.

Backups are still required because old versions of files and databases can be restored.

---

## Tests Performed

- Backup test successful
- Restore test successful
- Replication test successful
- Read-only page test successful
- Reboot test successful

---

## Repository Contents

- README.md
- cron.txt
- lemp-app
