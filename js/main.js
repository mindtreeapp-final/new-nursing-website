// Hero Banner Carousel
let currentSlide = 0;
let currentTextSlide = 0;
const heroSlides = document.querySelectorAll('.hero-slide');
const carouselTexts = document.querySelectorAll('.carousel-text');

function nextSlide() {
    if (heroSlides.length > 0) {
        heroSlides[currentSlide].classList.remove('active');
        currentSlide = (currentSlide + 1) % heroSlides.length;
        heroSlides[currentSlide].classList.add('active');
    }
}

function nextTextSlide() {
    if (carouselTexts.length > 0) {
        carouselTexts[currentTextSlide].classList.remove('active');
        currentTextSlide = (currentTextSlide + 1) % carouselTexts.length;
        carouselTexts[currentTextSlide].classList.add('active');
    }
}

// Auto slide images every 5 seconds
if (heroSlides.length > 0) {
    setInterval(nextSlide, 1000);
}

// Auto slide text every 3 seconds
if (carouselTexts.length > 0) {
    setInterval(nextTextSlide, 4000);
}

// Mobile menu toggle
const mobileMenuIcon = document.querySelector('.mobile-menu-icon');
const navMenu = document.querySelector('.nav-menu');
const dropdowns = document.querySelectorAll('.dropdown');

if (mobileMenuIcon) {
    mobileMenuIcon.addEventListener('click', () => {
        navMenu.classList.toggle('active');
    });
}

// Mobile dropdown functionality
dropdowns.forEach(dropdown => {
    const dropbtn = dropdown.querySelector('.dropbtn');
    if (dropbtn) {
        dropbtn.addEventListener('click', (e) => {
            if (window.innerWidth <= 768) {
                e.preventDefault();
                dropdown.classList.toggle('active');
            }
        });
    }
});

// Close mobile menu when clicking outside
document.addEventListener('click', (e) => {
    if (window.innerWidth <= 768) {
        if (!navMenu.contains(e.target) && !mobileMenuIcon.contains(e.target)) {
            navMenu.classList.remove('active');
            dropdowns.forEach(dropdown => dropdown.classList.remove('active'));
        }
    }
});

// Contact button - opens modal
const contactModal = document.getElementById('contact-modal');
const contactBtn = document.getElementById('contact-btn');
const closeBtns = document.getElementsByClassName('close');

// Terms & Conditions link
const termsLink = document.getElementById('terms-link');
if (termsLink) {
    termsLink.addEventListener('click', (e) => {
        e.preventDefault();
        // Replace 'YOUR_PDF_LINK_HERE' with your actual PDF link
        window.open('YOUR_PDF_LINK_HERE', '_blank');
    });
}

// Open Contact Modal
if (contactBtn) {
    contactBtn.addEventListener('click', (e) => {
        e.preventDefault();
        if (contactModal) {
            contactModal.style.display = 'block';
        }
    });
}

// Close modals
if (closeBtns.length > 0) {
    Array.from(closeBtns).forEach(btn => {
        btn.addEventListener('click', function() {
            this.parentElement.parentElement.style.display = 'none';
        });
    });
}

// Close modal when clicking outside
window.addEventListener('click', (e) => {
    if (contactModal && e.target === contactModal) {
        contactModal.style.display = 'none';
    }
});

// Course Card Click Handler
const courseCards = document.querySelectorAll('.course-card');
courseCards.forEach(card => {
    card.addEventListener('click', function() {
        const course = this.getAttribute('data-course');
        window.location.href = `course-detail.html?course=${course}`;
    });
});

// Chatbot Functionality
const chatbotTrigger = document.getElementById('chatbot-trigger');
const chatbot = document.getElementById('chatbot');
const chatbotClose = document.querySelector('.chatbot-close');
const chatInput = document.getElementById('chatInput');
const chatSend = document.getElementById('chatSend');
const chatMessages = document.getElementById('chatMessages');

// Chatbot knowledge base
const chatbotKnowledge = {
    greetings: ['hello', 'hi', 'hey', 'good morning', 'good afternoon', 'good evening'],
    courses: ['osce', 'oet', 'iqn', 'prometric', 'course', 'courses'],
    pricing: ['price', 'cost', 'fee', 'fees', 'pricing', 'how much'],
    contact: ['contact', 'phone', 'email', 'reach', 'call'],
    duration: ['duration', 'how long', 'time', 'period'],
    enrollment: ['enroll', 'register', 'join', 'admission', 'apply']
};

const chatbotResponses = {
    greeting: "Hello! Welcome to Mindtree Nursing Solutions. I'm here to help you with information about our courses. How can I assist you today?",
    courses: "We offer four main courses:\n1. OSCE - Objective Structured Clinical Examination\n2. OET - Occupational English Test\n3. IQN - International Qualification Network\n4. Prometric - Professional Licensing Exam\n\nWhich course would you like to know more about?",
    osce: "Our OSCE course provides comprehensive clinical skills training with:\n- Patient communication practice\n- Clinical scenarios\n- Mock examinations\n- Expert guidance\n\nWould you like to know about pricing or enrollment?",
    oet: "The OET course focuses on English language proficiency for healthcare professionals:\n- Reading & Writing modules\n- Listening skills\n- Speaking practice\n- Medical terminology\n\nInterested in enrolling?",
    iqn: "Our IQN program prepares you for international nursing qualifications with comprehensive training and support.",
    prometric: "The Prometric exam preparation includes:\n- Comprehensive review materials\n- Practice tests\n- Exam strategies\n- Study guides\n\nShall I help you get started?",
    pricing: "For detailed pricing information, please contact us at 1800-120-456-456 or fill out the Free Book form to speak with our admissions team.",
    contact: "You can reach us at:\n📞 Phone: 1800-120-456-456\n📧 Email: info@mindtreenursing.com\n💬 WhatsApp: Click the WhatsApp button below\n\nOur team is available Monday-Saturday, 9 AM - 6 PM.",
    duration: "Course durations vary:\n- OSCE: 3-6 months\n- OET: 2-4 months\n- IQN: 4-8 months\n- Prometric: 3-6 months\n\nWe also offer flexible scheduling to fit your needs.",
    enrollment: "To enroll in any course:\n1. Click the 'Enroll Now' or 'Free Book' button\n2. Fill out the form with your details\n3. Our team will contact you within 24 hours\n4. Complete the admission process\n\nWould you like me to open the enrollment form?",
    default: "I'm here to help! I can assist you with:\n- Course information\n- Pricing details\n- Enrollment process\n- Contact information\n\nWhat would you like to know?"
};

chatbotTrigger.addEventListener('click', () => {
    chatbot.style.display = 'flex';
});

chatbotClose.addEventListener('click', () => {
    chatbot.style.display = 'none';
});

function addMessage(message, isBot = true) {
    const messageDiv = document.createElement('div');
    messageDiv.className = isBot ? 'bot-message' : 'user-message';
    messageDiv.innerHTML = `<p>${message}</p>`;
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function getBotResponse(userMessage) {
    const message = userMessage.toLowerCase();
    
    // Check for greetings
    if (chatbotKnowledge.greetings.some(greeting => message.includes(greeting))) {
        return chatbotResponses.greeting;
    }
    
    // Check for course queries
    if (message.includes('osce')) {
        return chatbotResponses.osce;
    }
    if (message.includes('oet')) {
        return chatbotResponses.oet;
    }
    if (message.includes('iqn')) {
        return chatbotResponses.iqn;
    }
    if (message.includes('prometric')) {
        return chatbotResponses.prometric;
    }
    if (chatbotKnowledge.courses.some(keyword => message.includes(keyword))) {
        return chatbotResponses.courses;
    }
    
    // Check for pricing
    if (chatbotKnowledge.pricing.some(keyword => message.includes(keyword))) {
        return chatbotResponses.pricing;
    }
    
    // Check for contact
    if (chatbotKnowledge.contact.some(keyword => message.includes(keyword))) {
        return chatbotResponses.contact;
    }
    
    // Check for duration
    if (chatbotKnowledge.duration.some(keyword => message.includes(keyword))) {
        return chatbotResponses.duration;
    }
    
    // Check for enrollment
    if (chatbotKnowledge.enrollment.some(keyword => message.includes(keyword))) {
        return chatbotResponses.enrollment;
    }
    
    // Default response
    return chatbotResponses.default;
}

function sendMessage() {
    const message = chatInput.value.trim();
    if (message === '') return;
    
    // Add user message
    addMessage(message, false);
    chatInput.value = '';
    
    // Simulate typing delay
    setTimeout(() => {
        const response = getBotResponse(message);
        addMessage(response, true);
    }, 500);
}

chatSend.addEventListener('click', sendMessage);
chatInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Add animation on scroll
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observe elements for animation
document.querySelectorAll('.course-card, .offer-card, .category-card, .service-card').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'all 0.6s ease';
    observer.observe(el);
});

console.log('Mindtree Nursing Solutions - Website Loaded Successfully');