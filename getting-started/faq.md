# Frequently Asked Questions

Common questions and troubleshooting tips for getting Claude Code up and running.

> New to Claude Code? Start with [installing-claude.md](./installing-claude.md) first.

---

## Installation Issues

**Q: The installer says "command not found" after installation.**

Make sure your terminal's PATH includes the directory where Claude Code was installed. Try opening a new terminal window and running `claude --version` again.

**Q: I get a permission error when running the install script.**

Try running the install command with `sudo`, or check that you have write access to the install directory.

---

## Certificate & Zscaler Issues

**Q: I get SSL/TLS errors when Claude Code tries to connect.**

This is usually caused by Zscaler intercepting the connection. You need to add the Zscaler root certificate to your trusted certificates. See the [Zscaler Certificate Documentation](https://connect.sentinelone.com/site/b00a4fac-a250-505d-abfd-079c9f50f972/page/64426c1d-c34b-433c-a5f2-db32495d0dc3) for the correct certificate, then follow the steps in `installing-claude.md`.

**Q: Certificate errors only appear on the corporate network.**

This confirms it's a Zscaler issue. The certificate setup in `installing-claude.md` should resolve it. If you're still seeing errors after adding the certificate, try setting the `NODE_EXTRA_CA_CERTS` environment variable in your shell profile.

---

## Authentication

**Q: How do I log in to Claude Code?**

Run `claude` in your terminal — it will prompt you to authenticate via your browser on first launch.

**Q: My session expired. How do I re-authenticate?**

Run `claude` again and follow the login prompt. Sessions do expire periodically.

**Q: I don't have an Anthropic account. How do I get access?**

Contact a maintainer listed in the [README](../README.md) to get access through the team's account.

---

## General Usage

**Q: Claude Code seems slow. Is that normal?**

Response times vary based on the complexity of your request and network conditions. If it's consistently slow, check your network connection and VPN status.

**Q: Can I use Claude Code offline?**

No — Claude Code requires an internet connection to communicate with Anthropic's API.

**Q: Where can I find prompt templates to get started?**

Check the [`prompts/`](../prompts/) folder. It's organized by PM use case: discovery, strategy, execution, and analytics.

---

## Still Stuck?

- Check the [Anthropic documentation](https://docs.claude.ai)
- Reach out to a maintainer listed in the [README](../README.md)
- Open an issue in this repo to get help from the team
