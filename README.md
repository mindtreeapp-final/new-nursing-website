# Mindtree Nursing Solutions Website

Complete website for Mindtree Nursing Solutions - A professional nursing education platform.

## 📁 Project Structure

```
mindtree-nursing/
├── index.html              # Homepage with SEO
├── about.html              # About Us page
├── course-detail.html      # Dynamic course details with testimonials
├── site.webmanifest        # Web app manifest for favicon
├── css/
│   └── style.css          # Main stylesheet
├── js/
│   ├── main.js            # Main JavaScript functionality
│   └── course-detail.js   # Course page specific JavaScript
├── images/
│   ├── logo.png           # Your company logo
│   ├── favicon-16x16.png  # Favicon 16x16 (ADD THIS)
│   ├── favicon-32x32.png  # Favicon 32x32 (ADD THIS)
│   ├── apple-touch-icon.png # Apple touch icon 180x180 (ADD THIS)
│   ├── banner/            # Banner carousel images
│   │   ├── banner1.jpg
│   │   ├── banner2.jpg
│   │   └── banner3.jpg
│   ├── offers/            # Offer images
│   │   ├── offer1.jpg
│   │   └── offer2.jpg
│   ├── courses/           # Course hero images (ADD THESE)
│   │   ├── osce-hero.jpg
│   │   ├── oet-hero.jpg
│   │   ├── iqn-hero.jpg
│   │   ├── therapeutic-hero.jpg
│   │   └── interview-hero.jpg
│   └── team/              # Team member photos
│       ├── jeffy-john.jpg
│       ├── melvin-mathew.jpg
│       └── ... (all team photos)
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
2. **Add Favicon images:**
   - favicon-16x16.png (16x16 pixels)
   - favicon-32x32.png (32x32 pixels)
   - apple-touch-icon.png (180x180 pixels)
   - Use your logo and convert to these sizes using online tools
3. Add your company logo as `logo.png` in the `images` folder
4. **Add hero banner carousel images** (banner1.jpg, banner2.jpg, banner3.jpg) in `images/banner/`
5. **Add course hero images** in `images/courses/`:
   - osce-hero.jpg (1920x600 pixels)
   - oet-hero.jpg (1920x600 pixels)
   - iqn-hero.jpg (1920x600 pixels)
   - therapeutic-hero.jpg (1920x600 pixels)
   - interview-hero.jpg (1920x600 pixels)
6. Add offer images (offer1.jpg, offer2.jpg) in `images/offers/`
7. **Add team member photos** in `images/team/` folder
8. You can use placeholder images initially from https://placeholder.com/ or https://unsplash.com/

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

### Add Hero Banner Images
1. **Image Requirements:**
   - Size: 1920x600 pixels (wide format)
   - Format: JPG
   - Style: High-quality, professional nursing/healthcare images
   - Brightness: Not too dark (text appears over them)

2. **File Naming:**
   - banner1.jpg
   - banner2.jpg
   - banner3.jpg

3. **Place in:** `images/banner/` folder

4. **Image Suggestions:**
   - Nurses in professional settings
   - Hospital/clinic environments
   - International nursing themes
   - New Zealand landscapes with healthcare

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

## 🎥 Adding YouTube Videos to Course Pages

1. **Get YouTube Video IDs:**
   - Open your YouTube video
   - Look at the URL: `https://www.youtube.com/watch?v=ABC123XYZ`
   - The video ID is the part after `v=`: **ABC123XYZ**
   - For Shorts: `https://www.youtube.com/shorts/ABC123XYZ` - ID is **ABC123XYZ**

2. **Update course-detail.html:**
   - Find the video section in the HTML
   - Replace `YOUR_VIDEO_ID_1`, `YOUR_VIDEO_ID_2`, `YOUR_VIDEO_ID_3` with actual IDs
   - Example: Change `https://www.youtube.com/embed/YOUR_VIDEO_ID_1` 
     to `https://www.youtube.com/embed/ABC123XYZ`

3. **For YouTube Shorts:**
   - Shorts work the same way - just use the video ID
   - The embed will automatically adjust for vertical format

## 🔖 Create Favicon Files

### Option 1: Online Converter (Easiest)
1. Go to https://favicon.io/favicon-converter/
2. Upload your logo (PNG format)
3. Download the generated files
4. Extract and place in `images/` folder

### Option 2: Manual Creation
1. Open your logo in image editor (Photoshop, GIMP, etc.)
2. Create three versions:
   - 16x16 pixels → save as `favicon-16x16.png`
   - 32x32 pixels → save as `favicon-32x32.png`
   - 180x180 pixels → save as `apple-touch-icon.png`
3. Place all in `images/` folder

## 📱 Create Web Manifest File

Create a file named `site.webmanifest` in the root folder with this content:

```json
{
    "name": "Mindtree Nursing Solutions",
    "short_name": "Mindtree",
    "icons": [
        {
            "src": "/images/apple-touch-icon.png",
            "sizes": "180x180",
            "type": "image/png"
        }
    ],
    "theme_color": "#2563eb",
    "background_color": "#ffffff",
    "display": "standalone"
}
```

## 🎯 SEO Features Implemented

### ✅ Meta Tags Added
- **Title Tags**: Descriptive, keyword-rich titles on all pages
- **Meta Descriptions**: Unique descriptions for each page
- **Keywords**: Relevant nursing and education keywords
- **Robots**: Proper indexing instructions for search engines
- **Canonical URLs**: Prevent duplicate content issues

### ✅ Open Graph Tags
- **Facebook sharing**: Optimized preview when shared on Facebook
- **LinkedIn sharing**: Professional appearance on LinkedIn
- **Twitter Cards**: Enhanced previews on Twitter

### ✅ Structured Data
- Proper HTML5 semantic structure
- Heading hierarchy (H1, H2, H3)
- Alt text ready for images
- Descriptive link text

### ✅ Performance
- Fast loading times
- Mobile responsive
- Optimized images (when added)

### 📊 SEO Checklist for Launch

Before going live, complete these steps:

1. **Update URLs in Meta Tags:**
   - Replace `https://www.mindtreenursing.com` with your actual domain
   - Update all Open Graph URLs

2. **Add Image Alt Text:**
   - Add descriptive alt text to all images
   - Include keywords naturally

3. **Create Sitemap:**
   - Generate XML sitemap
   - Submit to Google Search Console

4. **Google Search Console:**
   - Verify your website
   - Submit sitemap
   - Check for crawl errors

5. **Google Analytics:**
   - Set up tracking code
   - Configure goals

6. **Page Speed:**
   - Test with Google PageSpeed Insights
   - Optimize images
   - Enable compression

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