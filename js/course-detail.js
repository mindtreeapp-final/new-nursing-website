// Course data
const courseData = {
    osce: {
        title: 'OSCE Preparation Course',
        subtitle: 'Objective Structured Clinical Examination Training',
        description: `
            <p>Our OSCE (Objective Structured Clinical Examination) preparation course is designed to help nursing professionals excel in their clinical assessment examinations. This comprehensive program covers all aspects of clinical skills evaluation, patient interaction, and practical nursing competencies required for international nursing practice.</p>
            <p>With experienced instructors who have international nursing backgrounds, you'll receive hands-on training with realistic clinical scenarios, standardized patient interactions, and detailed feedback to enhance your performance.</p>
        `,
        learningOutcomes: [
            'Master clinical assessment techniques and procedures',
            'Develop effective patient communication and interpersonal skills',
            'Practice with realistic clinical scenarios and simulations',
            'Learn proper documentation and reporting protocols',
            'Understand cultural competency in healthcare settings',
            'Build confidence for exam day through mock examinations',
            'Receive personalized feedback from expert assessors'
        ],
        targetAudience: `
            <p>This course is ideal for registered nurses planning to practice in countries like the UK, Australia, New Zealand, or other nations that require OSCE assessment. Whether you're a new graduate or an experienced nurse looking to work internationally, this program will prepare you for success.</p>
        `,
        duration: '3-6 Months',
        students: '300+',
        successRate: '96%',
        price: '₹45,000',
        modules: [
            {
                number: 1,
                title: 'Clinical Assessment Skills',
                topics: [
                    'Vital signs monitoring',
                    'Physical examination techniques',
                    'Patient assessment protocols',
                    'Documentation standards'
                ]
            },
            {
                number: 2,
                title: 'Communication Skills',
                topics: [
                    'Therapeutic communication',
                    'Patient education',
                    'Breaking bad news',
                    'Cultural sensitivity'
                ]
            },
            {
                number: 3,
                title: 'Clinical Procedures',
                topics: [
                    'Medication administration',
                    'Wound care management',
                    'Catheterization techniques',
                    'IV therapy'
                ]
            },
            {
                number: 4,
                title: 'Mock Examinations',
                topics: [
                    'Simulated OSCE stations',
                    'Timed practice sessions',
                    'Feedback and improvement',
                    'Exam day strategies'
                ]
            }
        ]
    },
    oet: {
        title: 'OET Training Program',
        subtitle: 'Occupational English Test for Healthcare Professionals',
        description: `
            <p>The Occupational English Test (OET) is specifically designed for healthcare professionals who wish to practice in English-speaking environments. Our comprehensive OET training program focuses on all four language skills - Reading, Writing, Listening, and Speaking - with a healthcare context.</p>
            <p>Our experienced trainers use proven methodologies to help you achieve the required grade for registration with healthcare regulatory bodies in countries like the UK, Australia, New Zealand, Dubai, and Singapore.</p>
        `,
        learningOutcomes: [
            'Develop advanced English language skills in healthcare context',
            'Master medical terminology and professional healthcare vocabulary',
            'Practice reading comprehension with healthcare texts',
            'Learn effective medical writing including referral letters',
            'Enhance listening skills with patient consultations',
            'Build confidence in speaking through role-plays',
            'Understand exam format and time management strategies'
        ],
        targetAudience: `
            <p>This course is perfect for nurses, doctors, dentists, and other healthcare professionals who need to demonstrate English language proficiency for professional registration or visa purposes in English-speaking countries.</p>
        `,
        duration: '2-4 Months',
        students: '500+',
        successRate: '95%',
        price: '₹35,000',
        modules: [
            {
                number: 1,
                title: 'Reading Skills',
                topics: [
                    'Healthcare texts comprehension',
                    'Medical journals and articles',
                    'Scanning and skimming techniques',
                    'Critical reading strategies'
                ]
            },
            {
                number: 2,
                title: 'Writing Skills',
                topics: [
                    'Referral letters',
                    'Transfer letters',
                    'Discharge summaries',
                    'Professional correspondence'
                ]
            },
            {
                number: 3,
                title: 'Listening Skills',
                topics: [
                    'Patient consultations',
                    'Healthcare lectures',
                    'Team meetings',
                    'Note-taking strategies'
                ]
            },
            {
                number: 4,
                title: 'Speaking Skills',
                topics: [
                    'Patient interviews',
                    'Giving advice and information',
                    'Building rapport',
                    'Professional dialogue'
                ]
            }
        ]
    },
    iqn: {
        title: 'IQN Certification Program',
        subtitle: 'International Qualification Network',
        description: `
            <p>The International Qualification Network (IQN) program is designed to help nursing professionals obtain international recognition of their qualifications. This comprehensive program prepares you for the assessment processes required by various international healthcare regulatory bodies.</p>
            <p>Our expert team guides you through the entire process, from documentation to skill assessment, ensuring you meet all requirements for international nursing practice.</p>
        `,
        learningOutcomes: [
            'Understand international nursing standards and requirements',
            'Prepare necessary documentation for qualification assessment',
            'Learn about different healthcare systems worldwide',
            'Develop skills for international nursing practice',
            'Navigate the qualification recognition process',
            'Meet competency standards for various countries',
            'Build professional portfolio for international applications'
        ],
        targetAudience: `
            <p>Ideal for registered nurses seeking international opportunities and needing to have their qualifications assessed and recognized by regulatory bodies in countries like Australia, New Zealand, Canada, and the UK.</p>
        `,
        duration: '4-8 Months',
        students: '200+',
        successRate: '93%',
        price: '₹50,000',
        modules: [
            {
                number: 1,
                title: 'Documentation Preparation',
                topics: [
                    'Academic credentials',
                    'Professional registration',
                    'Work experience verification',
                    'Reference letters'
                ]
            },
            {
                number: 2,
                title: 'Competency Assessment',
                topics: [
                    'Clinical skills evaluation',
                    'Theoretical knowledge testing',
                    'Professional standards',
                    'Regulatory requirements'
                ]
            },
            {
                number: 3,
                title: 'International Standards',
                topics: [
                    'Global nursing practices',
                    'Healthcare system variations',
                    'Cultural competency',
                    'Professional ethics'
                ]
            },
            {
                number: 4,
                title: 'Application Process',
                topics: [
                    'Regulatory body requirements',
                    'Application submission',
                    'Assessment procedures',
                    'Follow-up and support'
                ]
            }
        ]
    },
    prometric: {
        title: 'Prometric Exam Preparation',
        subtitle: 'Professional Nursing License Examination',
        description: `
            <p>The Prometric examination is a computer-based test required for nursing licensure in many countries, particularly in the Middle East. Our comprehensive preparation course covers all aspects of nursing knowledge and practice required to pass this challenging examination.</p>
            <p>With extensive question banks, practice tests, and expert instruction, we ensure you're thoroughly prepared for every topic covered in the Prometric exam.</p>
        `,
        learningOutcomes: [
            'Master comprehensive nursing theory and practice',
            'Understand Prometric exam format and question types',
            'Practice with extensive question banks',
            'Learn effective test-taking strategies',
            'Review all major nursing specialties',
            'Build confidence through mock examinations',
            'Identify and strengthen weak areas'
        ],
        targetAudience: `
            <p>This course is designed for registered nurses planning to work in Gulf countries (Saudi Arabia, UAE, Qatar, Kuwait, Oman, Bahrain) or other regions that require Prometric examination for nursing licensure.</p>
        `,
        duration: '3-6 Months',
        students: '400+',
        successRate: '94%',
        price: '₹40,000',
        modules: [
            {
                number: 1,
                title: 'Fundamentals of Nursing',
                topics: [
                    'Basic nursing concepts',
                    'Patient care principles',
                    'Infection control',
                    'Safety and quality'
                ]
            },
            {
                number: 2,
                title: 'Medical-Surgical Nursing',
                topics: [
                    'Common medical conditions',
                    'Surgical procedures',
                    'Post-operative care',
                    'Chronic disease management'
                ]
            },
            {
                number: 3,
                title: 'Specialized Areas',
                topics: [
                    'Pediatric nursing',
                    'Maternal health',
                    'Mental health nursing',
                    'Critical care'
                ]
            },
            {
                number: 4,
                title: 'Practice Tests',
                topics: [
                    'Full-length mock exams',
                    'Topic-wise assessments',
                    'Time management practice',
                    'Performance analysis'
                ]
            }
        ]
    },
    therapeutic: {
        title: 'Therapeutic Communication Course',
        subtitle: 'Professional Communication Skills for Healthcare',
        description: `
            <p>Our Therapeutic Communication course is designed to help healthcare professionals develop effective communication skills essential for patient care. This comprehensive program covers verbal and non-verbal communication techniques, active listening, empathy, and building therapeutic relationships with patients.</p>
            <p>With experienced instructors and practical scenarios, you'll learn how to communicate effectively in various healthcare settings, handle difficult conversations, and provide patient-centered care.</p>
        `,
        learningOutcomes: [
            'Master therapeutic communication techniques',
            'Develop active listening and empathy skills',
            'Handle difficult conversations professionally',
            'Build rapport with patients and families',
            'Understand cultural sensitivity in communication',
            'Practice effective non-verbal communication',
            'Learn conflict resolution strategies'
        ],
        targetAudience: `
            <p>This course is ideal for nurses and healthcare professionals who want to enhance their communication skills and provide better patient care. Whether you're a new graduate or an experienced professional, this course will strengthen your ability to connect with patients effectively.</p>
        `,
        duration: '2-3 Months',
        students: '250+',
        successRate: '97%',
        price: '₹30,000',
        modules: [
            {
                number: 1,
                title: 'Communication Fundamentals',
                topics: [
                    'Verbal communication techniques',
                    'Non-verbal communication',
                    'Active listening skills',
                    'Empathy and compassion'
                ]
            },
            {
                number: 2,
                title: 'Patient Interaction',
                topics: [
                    'Building therapeutic relationships',
                    'Patient-centered communication',
                    'Cultural competence',
                    'Family communication'
                ]
            },
            {
                number: 3,
                title: 'Difficult Conversations',
                topics: [
                    'Breaking bad news',
                    'Handling angry patients',
                    'Conflict resolution',
                    'Dealing with emotional situations'
                ]
            },
            {
                number: 4,
                title: 'Practical Application',
                topics: [
                    'Role-play scenarios',
                    'Case studies',
                    'Real-world practice',
                    'Feedback and improvement'
                ]
            }
        ]
    },
    interview: {
        title: 'Interview Preparation & Job Training',
        subtitle: 'Professional Interview Skills for Nursing Careers',
        description: `
            <p>Our Interview Preparation and Job Training course prepares nurses for successful job interviews in international healthcare settings. This comprehensive program covers interview techniques, professional presentation, common interview questions, and strategies to showcase your skills and experience effectively.</p>
            <p>With mock interviews, personalized feedback, and expert guidance, you'll gain the confidence and skills needed to excel in nursing job interviews and secure your dream position.</p>
        `,
        learningOutcomes: [
            'Master common nursing interview questions',
            'Develop professional presentation skills',
            'Create compelling responses using STAR method',
            'Understand cultural expectations in interviews',
            'Build confidence through mock interviews',
            'Learn salary negotiation techniques',
            'Prepare for video and phone interviews'
        ],
        targetAudience: `
            <p>This course is perfect for nurses preparing for job interviews in countries like New Zealand, Australia, UK, USA, Canada, and the Middle East. Whether you're applying for your first international position or advancing your nursing career, this training will give you a competitive edge.</p>
        `,
        duration: '1-2 Months',
        students: '350+',
        successRate: '96%',
        price: '₹25,000',
        modules: [
            {
                number: 1,
                title: 'Interview Fundamentals',
                topics: [
                    'Types of nursing interviews',
                    'Professional dress code',
                    'Body language and etiquette',
                    'First impressions'
                ]
            },
            {
                number: 2,
                title: 'Common Interview Questions',
                topics: [
                    'Clinical scenario questions',
                    'Behavioral questions',
                    'Situational questions',
                    'STAR method responses'
                ]
            },
            {
                number: 3,
                title: 'Mock Interviews',
                topics: [
                    'Practice interviews',
                    'Personalized feedback',
                    'Video interview techniques',
                    'Phone interview skills'
                ]
            },
            {
                number: 4,
                title: 'Job Search Strategy',
                topics: [
                    'Resume optimization',
                    'Cover letter writing',
                    'Salary negotiation',
                    'Follow-up techniques'
                ]
            }
        ]
    }
};

// Get course parameter from URL
function getCourseFromURL() {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get('course') || 'osce';
}

// Load course data
function loadCourseData() {
    const courseType = getCourseFromURL();
    const course = courseData[courseType];
    
    if (!course) {
        window.location.href = 'index.html';
        return;
    }
    
    // Update page title and meta
    document.title = `${course.title} - Mindtree Nursing Solutions`;
    
    // Update hero section
    document.getElementById('course-title').textContent = course.title;
    document.getElementById('course-subtitle').textContent = course.subtitle;
    
    // Update stats
    document.getElementById('stat-students').textContent = course.students;
    document.getElementById('stat-success').textContent = course.successRate;
    document.getElementById('stat-duration').textContent = course.duration;
    
    // Update main content
    document.getElementById('course-description').innerHTML = course.description;
    
    // Update learning outcomes
    const outcomesHTML = course.learningOutcomes
        .map(outcome => `<li>${outcome}</li>`)
        .join('');
    document.getElementById('learning-outcomes').innerHTML = outcomesHTML;
    
    // Update target audience
    document.getElementById('target-audience').innerHTML = course.targetAudience;
    
    // Update price
    document.getElementById('course-price').textContent = course.price;
    
    // Update curriculum
    const curriculumHTML = course.modules
        .map(module => `
            <div class="module-card">
                <div class="module-number">${module.number}</div>
                <h3>${module.title}</h3>
                <ul>
                    ${module.topics.map(topic => `<li>${topic}</li>`).join('')}
                </ul>
            </div>
        `)
        .join('');
    document.getElementById('curriculum-container').innerHTML = curriculumHTML;
    
    // Pre-select course in form dropdown
    const courseSelect = document.getElementById('course');
    if (courseSelect) {
        const courseName = course.title.split(' ')[0].toUpperCase();
        for (let option of courseSelect.options) {
            if (option.value === courseName) {
                option.selected = true;
                break;
            }
        }
    }
}

// Initialize page
document.addEventListener('DOMContentLoaded', loadCourseData);