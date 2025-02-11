document.getElementById('contact-form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    // Here you would typically send the form data to a server
    alert('Thank you for your message! I will get back to you soon.');
    this.reset();
});

// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Mobile menu toggle
const menuToggle = document.querySelector('.menu-toggle');
const navLinks = document.querySelector('.nav-links');

menuToggle.addEventListener('click', () => {
    navLinks.classList.toggle('active');
});

// Lazy loading for videos
document.addEventListener('DOMContentLoaded', function() {
    const videos = document.querySelectorAll('video');
    
    const videoObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const video = entry.target;
                video.src = video.dataset.src;
                videoObserver.unobserve(video);
            }
        });
    });

    videos.forEach(video => {
        videoObserver.observe(video);
    });
});

// Smooth reveal animation for projects
const revealElements = document.querySelectorAll('.media-item');

const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('revealed');
        }
    });
}, {
    threshold: 0.1
});

revealElements.forEach(element => {
    revealObserver.observe(element);
}); 