# Mindtree Nursing Solutions Website

Complete website for Mindtree Nursing Solutions - A professional nursing education platform.

## 📁 Project Structure

```
mindtree-nursing/
├── index.html              # Homepage
├── about.html              # About Us page with team details
├── course-detail.html      # Dynamic course details page
├── css/
│   └── style.css          # Main stylesheet
├── js/
│   ├── main.js            # Main JavaScript functionality
│   └── course-detail.js   # Course page specific JavaScript
├── images/
│   ├── logo.png           # Your company logo (ADD THIS)
│   ├── banner/            # Banner images
│   ├── offers/            # Offer images (ADD THESE)
│   │   ├── offer1.jpg
│   │   └── offer2.jpg
│   ├── courses/           # Course related images
│   └── team/              # Team member photos (ADD THESE)
│       ├── jeffy-john.jpg
│       ├── melvin-mathew.jpg
│       ├── joby-john.jpg
│       ├── anju-iype.jpg
│       ├── surya-m.jpg
│       ├── reshma-vr.jpg
│       ├── nandan-r-ajay.jpg
│       ├── edbin.jpg
│       ├── sujith-padmanabhan.jpg
│       ├── rimy-mathew.jpg
│       ├── arya-mohan.jpg
│       ├── sreeja-s.jpg
│       ├── raji-o.jpg
│       ├── bincymol-s.jpg
│       ├── reena-babu.jpg
│       ├── priya-philip.jpg
│       ├── reena-roy.jpg
│       ├── rincy.jpg
│       ├── anuja.jpg
│       ├── anu.jpg
│       └── anugraha.jpg
└── README.md
```

## 🚀 Setup Instructions in VSCode

### Step 1: Install Visual Studio Code
1. Download VSCode from https://code.visualstudio.com/
2. Install and open VSCode

### Step 2: Install Required Extension
1. Open VSCode
2. Go to Extensions (Ctrl+Shift+X or Cmd+Shift+X on Mac)
3. Search for "Live Server" by Ritwick Dey
4. Click Install

### Step 3: Create Project
1. Create a new folder called `mindtree-nursing` on your desktop
2. Open VSCode
3. File → Open Folder → Select `mindtree-nursing` folder
4. Create the folder structure shown above

### Step 4: Add Files
1. Copy all the code I provided into their respective files:
   - Create `index.html` and paste the homepage code
   - Create `about.html` and paste the about page code
   - Create `course-detail.html` and paste the course detail code
   - Create `css` folder and add `style.css`
   - Create `js` folder and add `main.js` and `course-detail.js`

### Step 5: Add Images
1. Create the `images` folder structure
2. Add your company logo as `logo.png` in the `images` folder
3. Add offer images (offer1.jpg, offer2.jpg) in `images/offers/`
4. **Add team member photos** in `images/team/` folder:
   - **Directors:** jeffy-john.jpg, melvin-mathew.jpg
   - **Team Members:** joby-john.jpg, anju-iype.jpg, surya-m.jpg, reshma-vr.jpg, nandan-r-ajay.jpg, edbin.jpg, sujith-padmanabhan.jpg, rimy-mathew.jpg, arya-mohan.jpg, sreeja-s.jpg, raji-o.jpg, bincymol-s.jpg, reena-babu.jpg, priya-philip.jpg, reena-roy.jpg, rincy.jpg, anuja.jpg, anu.jpg, anugraha.jpg
   - **Image specs:** 400x400 pixels (square), JPG format, professional headshots
   - **Note:** If images are missing, fallback icons will display automatically
5. You can use placeholder images initially from https://placeholder.com/ or https://unsplash.com/

### Step 6: Run the Website
1. Right-click on `index.html` in VSCode
2. Select "Open with Live Server"
3. Your website will open in the browser at `http://127.0.0.1:5500/`

## 🎨 Features Implemented

### ✅ Navigation
- Sticky navigation bar with company logo
- Dropdown menus for Courses and App
- Contact Us button
- Free Book button with form

### ✅ Homepage
- Hero banner with achievement badges
- Popular courses slider
- Special offers section
- Explore courses section with detailed cards
- Fixed WhatsApp and chatbot buttons

### ✅ About Us Page
- Company story and mission
- Core values section
- Team members with details (6 employees)
- Professional layout

### ✅ Course Detail Pages
- Dynamic content based on URL parameter
- Comprehensive course information
- Curriculum modules
- Student testimonials
- Enrollment sidebar

### ✅ Forms & Modals
- Contact Us modal with phone number
- Free Book form with Zoho CRM integration
- Success messages

### ✅ Chatbot
- Trained AI chatbot
- Answers queries about:
  - Courses (OSCE, OET, IQN, Prometric)
  - Pricing
  - Contact information
  - Duration
  - Enrollment process
- Natural conversation flow

### ✅ Mobile Responsive
- Fully responsive design
- Works on all devices

## 🔧 Customization Guide

### Change Company Logo
1. Replace `images/logo.png` with your logo
2. Recommended size: 200x50 pixels or similar ratio
3. Format: PNG with transparent background

### Update Phone Number
Search for `1800-120-456-456` in all files and replace with your number.

### Update WhatsApp Link
1. Find `https://wa.me/1234567890` in `index.html`, `about.html`, and `course-detail.html`
2. Replace with your WhatsApp number (format: country code + number without + or spaces)
3. Example: `https://wa.me/919876543210`

### Update App Store Links
1. Find the App dropdown section in navigation
2. Replace iOS link: `https://apps.apple.com/your-app`
3. Replace Android link: `https://play.google.com/store/apps/your-app`

### Add Offer Images
1. Create images sized 600x400 pixels
2. Name them: offer1.jpg, offer2.jpg
3. Place in `images/offers/` folder

### Add Team Member Photos
1. **Image Requirements:**
   - Size: 400x400 pixels (square format)
   - Format: JPG
   - Style: Professional headshots with good lighting
   - Background: Plain or professional setting

2. **File Naming:** Use lowercase with hyphens
   - Example: `jeffy-john.jpg`, `melvin-mathew.jpg`

3. **All Team Photos Needed (21 total):**
   - **Directors (2):** jeffy-john.jpg, melvin-mathew.jpg
   - **Team (19):** joby-john.jpg, anju-iype.jpg, surya-m.jpg, reshma-vr.jpg, nandan-r-ajay.jpg, edbin.jpg, sujith-padmanabhan.jpg, rimy-mathew.jpg, arya-mohan.jpg, sreeja-s.jpg, raji-o.jpg, bincymol-s.jpg, reena-babu.jpg, priya-philip.jpg, reena-roy.jpg, rincy.jpg, anuja.jpg, anu.jpg, anugraha.jpg

4. **Fallback System:**
   - If an image is missing, an icon will display automatically
   - This allows you to add photos gradually

5. **Tips for Best Results:**
   - Use consistent lighting across all photos
   - Same background color/style creates unity
   - Crop photos to show head and shoulders
   - Ensure faces are centered and clearly visible

### Change Colors
Edit the color variables in `css/style.css`:
```css
:root {
    --primary-color: #2563eb;      /* Main blue color */
    --secondary-color: #10b981;    /* Green accent */
    --accent-color: #f59e0b;       /* Orange accent */
}
```

## 🔗 Zoho CRM Integration

### Setting Up Zoho CRM
1. Create a Zoho CRM account at https://www.zoho.com/crm/
2. Go to Setup → Developer Space → APIs
3. Create a Server-based Application
4. Generate Access Token
5. Update the token in `js/main.js`:

```javascript
// Find this line in main.js
'Authorization': 'Zoho-oauthtoken YOUR_ACCESS_TOKEN_HERE',

// Replace YOUR_ACCESS_TOKEN_HERE with your actual token
```

### Form Fields Sent to Zoho
- Name
- Phone Number
- Email
- Course Interest
- Timestamp

## 📱 Testing the Website

### Test Checklist
- [ ] Homepage loads correctly
- [ ] Navigation dropdowns work
- [ ] Click on each course card
- [ ] Test Contact Us modal
- [ ] Test Free Book form
- [ ] Click WhatsApp button
- [ ] Test chatbot with different queries
- [ ] Test on mobile view (Chrome DevTools → Toggle Device Toolbar)
- [ ] Check all internal links work
- [ ] Verify About Us page displays team members

## 🤖 Chatbot Training

The chatbot is pre-trained to answer:
- Greetings: "Hello", "Hi", "Hey"
- Course queries: Asks about OSCE, OET, IQN, Prometric
- Pricing information
- Contact details
- Course duration
- Enrollment process

To add more responses, edit the `chatbotKnowledge` and `chatbotResponses` objects in `js/main.js`.

## 🌐 Publishing the Website

### Option 1: Netlify (Recommended - Free)
1. Create account at https://www.netlify.com/
2. Drag and drop your project folder
3. Your site goes live in seconds!

### Option 2: GitHub Pages (Free)
1. Create GitHub account
2. Create new repository
3. Upload your files
4. Enable GitHub Pages in settings

### Option 3: Traditional Hosting
1. Buy hosting from providers like Hostinger, Bluehost, GoDaddy
2. Upload files via FTP using FileZilla
3. Point your domain to the hosting

## 💡 Tips for Success

1. **Use High-Quality Images**: Professional photos make a huge difference
2. **Test on Multiple Browsers**: Chrome, Firefox, Safari, Edge
3. **Mobile Testing**: Most users browse on mobile
4. **Update Content Regularly**: Keep course info current
5. **Monitor Form Submissions**: Check Zoho CRM regularly
6. **SEO Optimization**: Add meta descriptions and keywords later

## 📞 Support

For issues or questions about this website:
1. Check all file paths are correct
2. Ensure images are in the right folders
3. Verify Live Server extension is running
4. Check browser console for errors (F12)

## 🎯 Next Steps

After setting up the basic website:
1. Add your actual images and logo
2. Set up Zoho CRM integration
3. Update all contact information
4. Test thoroughly on different devices
5. Get feedback from colleagues
6. Deploy to a hosting platform
7. Set up Google Analytics for tracking
8. Configure email notifications for form submissions

## 📄 License

This website is created for Mindtree Nursing Solutions. All rights reserved.

---

**Built with ❤️ for Mindtree Nursing Solutions**

Website Version: 1.0
Last Updated: January 2025