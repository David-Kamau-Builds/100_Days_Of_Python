document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    const inputs = document.querySelectorAll('input, textarea');

    inputs.forEach(input => {
        input.addEventListener('focus', function () {
            this.parentElement.style.transform = 'translateY(-2px)';
        });

        input.addEventListener('blur', function () {
            this.parentElement.style.transform = 'translateY(0)';
        });

        input.addEventListener('input', function () {
            if (this.checkValidity()) {
                this.style.borderColor = '#2ecc71';
            } else {
                this.style.borderColor = '#e74c3c';
            }
        });
    });

    form.addEventListener('submit', function (e) {
        e.preventDefault();

        let isValid = true;
        inputs.forEach(input => {
            if (!input.checkValidity()) {
                isValid = false;
                input.style.borderColor = '#e74c3c';
            }
        });

        if (isValid) {
            const submitBtn = document.querySelector('.submit-btn');
            const originalText = submitBtn.innerHTML;

            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sending...';
            submitBtn.disabled = true;

            setTimeout(() => {
                submitBtn.innerHTML = '<i class="fas fa-check"></i> Message Sent!';
                submitBtn.style.background = 'linear-gradient(90deg, #27ae60, #2ecc71)';

                setTimeout(() => {
                    form.reset();
                    submitBtn.innerHTML = originalText;
                    submitBtn.disabled = false;
                    submitBtn.style.background = 'linear-gradient(90deg, #3498db, #2ecc71)';

                    inputs.forEach(input => {
                        input.style.borderColor = '#e1e8ed';
                    });
                }, 2000);
            }, 1500);
        }
    });
});