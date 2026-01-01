// Add some interactivity
        document.addEventListener('DOMContentLoaded', function() {
            const form = document.querySelector('form');
            const inputs = document.querySelectorAll('input, textarea');
            
            // Add focus effects
            inputs.forEach(input => {
                // Add focus class to parent on input focus
                input.addEventListener('focus', function() {
                    this.parentElement.style.transform = 'translateY(-2px)';
                });
                
                // Remove focus class from parent on input blur
                input.addEventListener('blur', function() {
                    this.parentElement.style.transform = 'translateY(0)';
                });
                
                // Add validation styling
                input.addEventListener('input', function() {
                    if (this.checkValidity()) {
                        this.style.borderColor = '#2ecc71';
                    } else {
                        this.style.borderColor = '#e74c3c';
                    }
                });
            });
            
            // Form submission animation
            form.addEventListener('submit', function(e) {
                // In a real application, you would prevent default only if validation fails
                // For demo purposes, we'll show a success message
                e.preventDefault();
                
                // Simple validation
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
                    
                    // Show loading state
                    submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sending...';
                    submitBtn.disabled = true;
                    
                    // Simulate API call
                    setTimeout(() => {
                        // Show success state
                        submitBtn.innerHTML = '<i class="fas fa-check"></i> Message Sent!';
                        submitBtn.style.background = 'linear-gradient(90deg, #27ae60, #2ecc71)';
                        
                        // Reset form after 2 seconds
                        setTimeout(() => {
                            form.reset();
                            submitBtn.innerHTML = originalText;
                            submitBtn.disabled = false;
                            submitBtn.style.background = 'linear-gradient(90deg, #3498db, #2ecc71)';
                            
                            // Reset input borders
                            inputs.forEach(input => {
                                input.style.borderColor = '#e1e8ed';
                            });
                        }, 2000);
                    }, 1500);
                }
            });
        });