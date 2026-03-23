# 002 — Fix SSH Host Key

**Date**: 2026-03-23
**Tool**: GitHub Copilot
**Model**: Grok Code Fast 1
**Iterations**: 1

## Prompt

**2026-03-23 00:00**

cd /home/lara/Documents/AcceleratingSoftwareEngingeeringWithAI/RePo-SO/so-challenge
gh repo create so-challenge --public --source=. --push
✓ Created repository sileju/so-challenge on GitHub
  https://github.com/sileju/so-challenge
✓ Added remote git@github.com:sileju/so-challenge.git
The authenticity of host 'github.com (140.82.121.4)' can't be established.
ED25519 key fingerprint is SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? 
Host key verification failed.
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
failed to run git: exit status 128 I ACCIDENTALY PRESSED ENTER INDSTEAD OF TYPING YES. HOW CAN I CORRECT THIS MISTAKE