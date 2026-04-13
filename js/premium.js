document.addEventListener('DOMContentLoaded', () => {
    // Scroll Reveal Animation
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('reveal-active');
            }
        });
    }, observerOptions);

    const revealElements = document.querySelectorAll('.hero-text, .hero-image, .program-card, .section-title, .testimonial-card');
    
    // Set initial styles for reveal
    revealElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'all 0.8s cubic-bezier(0.4, 0, 0.2, 1)';
    });

    // Add reveal logic
    const style = document.createElement('style');
    style.innerHTML = `
        .reveal-active {
            opacity: 1 !important;
            transform: translateY(0) !important;
        }
    `;
    document.head.appendChild(style);

    revealElements.forEach(el => revealObserver.observe(el));

    // Counter Animation
    const stats = document.querySelectorAll('.stat-item h3');
    stats.forEach(stat => {
        const targetValue = parseInt(stat.innerText);
        let currentValue = 0;
        const duration = 2000;
        const stepTime = duration / targetValue;

        const counter = setInterval(() => {
            currentValue += Math.ceil(targetValue / 100);
            if (currentValue >= targetValue) {
                stat.innerText = targetValue + (stat.innerText.includes('%') ? '%' : '+');
                clearInterval(counter);
            } else {
                stat.innerText = currentValue + (stat.innerText.includes('%') ? '%' : '+');
            }
        }, 20);
    });
});
