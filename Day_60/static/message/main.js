document.addEventListener('DOMContentLoaded', function() {
            document.querySelector('footer p').innerHTML = `© ${new Date().getFullYear()} Contact Form. All rights reserved.`;

            const redirectTimer = document.createElement('div');
            redirectTimer.className = 'redirect-timer';
            redirectTimer.innerHTML = '<i class="fas fa-clock"></i> You will be redirected to home page in <span id="countdown">30</span> seconds...';
            document.querySelector('.action-buttons').parentNode.insertBefore(redirectTimer, document.querySelector('.confirmation-note'));

            let countdown = 30;
            const countdownElement = document.getElementById('countdown');
            const countdownInterval = setInterval(() => {
                countdown--;
                countdownElement.textContent = countdown;

                if (countdown <= 0) {
                    clearInterval(countdownInterval);
                    window.location.href = document.body.dataset.indexUrl;
                }
            }, 1000);

            const confirmationId = document.querySelector('.confirmation-id');
            confirmationId.style.cursor = 'pointer';
            confirmationId.title = 'Click to copy Confirmation ID';

            confirmationId.addEventListener('click', function() {
                const textToCopy = this.textContent;
                navigator.clipboard.writeText(textToCopy).then(() => {
                    const originalText = this.textContent;
                    this.innerHTML = '<i class="fas fa-check"></i> Copied!';
                    this.style.color = '#2ecc71';

                    setTimeout(() => {
                        this.textContent = originalText;
                        this.style.color = '';
                    }, 2000);
                });
            });

            const messagePreview = document.querySelector('.message-preview');
            const fullMessage = messagePreview.textContent;
            if (fullMessage.length > 200) {
                messagePreview.textContent = fullMessage.substring(0, 200) + '...';
                messagePreview.title = fullMessage;
                messagePreview.style.cursor = 'help';
            }
        });