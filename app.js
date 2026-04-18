/**
 * riera.co.uk — app.js
 * Handles: scroll reveal animations, mobile nav toggle, audit form submission.
 */

/* ── Scroll reveal via IntersectionObserver ── */
(function initReveal() {
    const els = document.querySelectorAll(".reveal");
    if (!els.length) return;

    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("is-visible");
                    observer.unobserve(entry.target);
                }
            });
        },
        { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
    );

    els.forEach((el) => observer.observe(el));
})();

/* ── Mobile nav toggle ── */
(function initNav() {
    const toggle = document.getElementById("nav-toggle");
    const nav = document.getElementById("main-nav");
    if (!toggle || !nav) return;

    toggle.addEventListener("click", () => {
        const open = nav.classList.toggle("is-open");
        toggle.classList.toggle("is-active", open);
        toggle.setAttribute("aria-expanded", open);
    });

    // Close nav when a link is clicked
    nav.querySelectorAll("a").forEach((link) => {
        link.addEventListener("click", () => {
            nav.classList.remove("is-open");
            toggle.classList.remove("is-active");
            toggle.setAttribute("aria-expanded", "false");
        });
    });
})();

/* ── Audit form submission (n8n webhook) ── */
(function initForm() {
    const form = document.getElementById("audit-form");
    const statusEl = document.getElementById("form-status");
    if (!form || !statusEl) return;

    form.addEventListener("submit", async (event) => {
        event.preventDefault();
        if (!form.reportValidity()) return;

        const button = form.querySelector("button[type='submit']");
        const payload = {
            name: form.name.value.trim(),
            email: form.email.value.trim(),
            company: form.company.value.trim(),
            website: form.website.value.trim(),
            team_size: form.team_size.value,
            current_tools: form.current_tools.value.trim(),
            repetitive_process: form.repetitive_process.value.trim(),
            admin_time_lost: form.admin_time_lost.value,
            desired_outcome: form.desired_outcome.value.trim(),
            contact_consent: form.contact_consent.checked,
            source: "riera.co.uk"
        };

        button.disabled = true;
        button.textContent = "Sending…";
        statusEl.className = "form-status";
        statusEl.textContent = "";

        try {
            const response = await fetch(
                "https://n8n.joanmarcriera.es/webhook/automation-audit-intake",
                {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify(payload)
                }
            );

            if (!response.ok) {
                throw new Error("Request failed: " + response.status);
            }

            form.reset();
            statusEl.classList.add("is-success");
            statusEl.textContent =
                "Audit request sent. I will follow up after qualification.";
        } catch (err) {
            statusEl.classList.add("is-error");
            statusEl.innerHTML =
                'Submission failed. Email <a href="mailto:joanmarcriera@gmail.com">joanmarcriera@gmail.com</a> and mention "Automation Audit".';
        } finally {
            button.disabled = false;
            button.textContent = "Send Audit Request";
        }
    });
})();
