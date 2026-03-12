const form = document.getElementById("audit-form");
const statusEl = document.getElementById("form-status");

if (form && statusEl) {
    form.addEventListener("submit", async (event) => {
        event.preventDefault();

        if (!form.reportValidity()) {
            return;
        }

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
        button.textContent = "Sending...";
        statusEl.className = "form-status";
        statusEl.textContent = "";

        try {
            const response = await fetch("https://n8n.joanmarcriera.es/webhook/automation-audit-intake", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(payload)
            });

            if (!response.ok) {
                throw new Error(`Request failed with status ${response.status}`);
            }

            form.reset();
            statusEl.classList.add("is-success");
            statusEl.textContent = "Audit request sent. I will follow up after qualification and payment review.";
        } catch (error) {
            statusEl.classList.add("is-error");
            statusEl.innerHTML = 'The form could not be submitted right now. Email <a href="mailto:joanmarcriera@gmail.com">joanmarcriera@gmail.com</a> and mention "Automation Audit".';
        } finally {
            button.disabled = false;
            button.textContent = "Send Audit Request";
        }
    });
}
