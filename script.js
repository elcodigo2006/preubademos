document.addEventListener('DOMContentLoaded', function() {
    const menuBtn = document.querySelector('header nav button');
    const mobileNav = document.querySelector('header nav ul');
    const header = document.querySelector('header');

    // Hover effects for buttons and links
    document.querySelectorAll('button, a').forEach(element => {
        element.addEventListener('mouseenter', () => {
            element.style.transform = 'scale(1.05)';
            element.classList.add('hovered');
        });
        element.addEventListener('mouseleave', () => {
            element.style.transform = 'scale(1)';
            element.classList.remove('hovered');
        });
    });

    // Toggle mobile menu
    menuBtn.addEventListener('click', () => {
        mobileNav.classList.toggle('active');
        if (mobileNav.classList.contains('active')) {
            menuBtn.textContent = 'Cerrar';
        } else {
            menuBtn.textContent = 'Reservar';
        }
    });

    // Scroll behavior for navbar
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });

    // Reveal sections on scroll
    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('reveal-visible');
            }
        });
    }, { threshold: 0.25 });

    document.querySelectorAll('.card, .review-card').forEach(section => {
        observer.observe(section);
    });
});