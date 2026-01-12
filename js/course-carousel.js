// ============================================
// TESTIMONIALS/REVIEWS CAROUSEL (Course Pages)
// ============================================
document.addEventListener('DOMContentLoaded', () => {
    const reviewsTrack = document.getElementById('reviewsTrack');
    const reviewCards = document.querySelectorAll('.reviews-carousel .review-card');
    const reviewsPrevBtn = document.getElementById('reviewsPrev');
    const reviewsNextBtn = document.getElementById('reviewsNext');
    const reviewDots = document.querySelectorAll('.reviews-carousel .carousel-dot');
    
    if (reviewCards.length === 0) {
        console.log('No review cards found');
        return; // Exit if no reviews found
    }
    
    let currentReviewIndex = 0;

    function updateActiveReview() {
        reviewCards.forEach((card, index) => {
            card.classList.remove('active');
            if (index === currentReviewIndex) {
                card.classList.add('active');
            }
        });
        
        reviewDots.forEach((dot, index) => {
            dot.classList.remove('active');
            if (index === currentReviewIndex) {
                dot.classList.add('active');
            }
        });
    }

    function scrollToReview(index) {
        if (!reviewsTrack || !reviewCards[index]) return;
        
        const card = reviewCards[index];
        const trackRect = reviewsTrack.getBoundingClientRect();
        const cardRect = card.getBoundingClientRect();
        const scrollLeft = card.offsetLeft - (trackRect.width / 2) + (cardRect.width / 2);
        
        reviewsTrack.scrollTo({
            left: scrollLeft,
            behavior: 'smooth'
        });
        
        currentReviewIndex = index;
        updateActiveReview();
    }

    if (reviewsPrevBtn) {
        reviewsPrevBtn.addEventListener('click', (e) => {
            e.preventDefault();
            const newIndex = currentReviewIndex > 0 ? currentReviewIndex - 1 : reviewCards.length - 1;
            scrollToReview(newIndex);
        });
    }

    if (reviewsNextBtn) {
        reviewsNextBtn.addEventListener('click', (e) => {
            e.preventDefault();
            const newIndex = currentReviewIndex < reviewCards.length - 1 ? currentReviewIndex + 1 : 0;
            scrollToReview(newIndex);
        });
    }

    // Dot navigation for reviews
    reviewDots.forEach((dot) => {
        dot.addEventListener('click', (e) => {
            e.preventDefault();
            const index = parseInt(dot.getAttribute('data-index'));
            scrollToReview(index);
        });
    });

    // Handle scroll event to update active review
    if (reviewsTrack) {
        let scrollTimeout;
        reviewsTrack.addEventListener('scroll', () => {
            clearTimeout(scrollTimeout);
            scrollTimeout = setTimeout(() => {
                const scrollPosition = reviewsTrack.scrollLeft;
                const cardWidth = reviewCards[0]?.offsetWidth || 0;
                const gap = 30;
                const newIndex = Math.round(scrollPosition / (cardWidth + gap));
                
                if (newIndex !== currentReviewIndex && newIndex >= 0 && newIndex < reviewCards.length) {
                    currentReviewIndex = newIndex;
                    updateActiveReview();
                }
            }, 150);
        });
    }

    // Initialize
    updateActiveReview();
    console.log('Reviews carousel initialized with', reviewCards.length, 'cards');
});

// ============================================
// VIDEOS CAROUSEL (Course Pages)
// ============================================
document.addEventListener('DOMContentLoaded', () => {
    const videosTrack = document.getElementById('videosTrack');
    const videoCards = document.querySelectorAll('.videos-carousel .video-card');
    const videosPrevBtn = document.getElementById('videosPrev');
    const videosNextBtn = document.getElementById('videosNext');
    const videoDots = document.querySelectorAll('.videos-carousel .carousel-dot');
    
    if (videoCards.length === 0) {
        console.log('No video cards found');
        return; // Exit if no videos found
    }
    
    let currentVideoIndex = 0;

    function updateActiveVideo() {
        videoCards.forEach((card, index) => {
            card.classList.remove('active');
            if (index === currentVideoIndex) {
                card.classList.add('active');
            }
        });
        
        videoDots.forEach((dot, index) => {
            dot.classList.remove('active');
            if (index === currentVideoIndex) {
                dot.classList.add('active');
            }
        });
    }

    function scrollToVideo(index) {
        if (!videosTrack || !videoCards[index]) return;
        
        const card = videoCards[index];
        const trackRect = videosTrack.getBoundingClientRect();
        const cardRect = card.getBoundingClientRect();
        const scrollLeft = card.offsetLeft - (trackRect.width / 2) + (cardRect.width / 2);
        
        videosTrack.scrollTo({
            left: scrollLeft,
            behavior: 'smooth'
        });
        
        currentVideoIndex = index;
        updateActiveVideo();
    }

    if (videosPrevBtn) {
        videosPrevBtn.addEventListener('click', (e) => {
            e.preventDefault();
            const newIndex = currentVideoIndex > 0 ? currentVideoIndex - 1 : videoCards.length - 1;
            scrollToVideo(newIndex);
        });
    }

    if (videosNextBtn) {
        videosNextBtn.addEventListener('click', (e) => {
            e.preventDefault();
            const newIndex = currentVideoIndex < videoCards.length - 1 ? currentVideoIndex + 1 : 0;
            scrollToVideo(newIndex);
        });
    }

    // Dot navigation for videos
    videoDots.forEach((dot) => {
        dot.addEventListener('click', (e) => {
            e.preventDefault();
            const index = parseInt(dot.getAttribute('data-index'));
            scrollToVideo(index);
        });
    });

    // Handle scroll event to update active video
    if (videosTrack) {
        let scrollTimeout;
        videosTrack.addEventListener('scroll', () => {
            clearTimeout(scrollTimeout);
            scrollTimeout = setTimeout(() => {
                const scrollPosition = videosTrack.scrollLeft;
                const cardWidth = videoCards[0]?.offsetWidth || 0;
                const gap = 30;
                const newIndex = Math.round(scrollPosition / (cardWidth + gap));
                
                if (newIndex !== currentVideoIndex && newIndex >= 0 && newIndex < videoCards.length) {
                    currentVideoIndex = newIndex;
                    updateActiveVideo();
                }
            }, 150);
        });
    }

    // Initialize
    updateActiveVideo();
    console.log('Videos carousel initialized with', videoCards.length, 'cards');
});

console.log('Course carousel script loaded successfully');