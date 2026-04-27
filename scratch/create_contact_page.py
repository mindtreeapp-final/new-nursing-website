import re

def create_contact_page():
    with open('d:/editable web/index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract the header and nav part
    # up to the end of </nav>
    nav_end = content.find('</nav>') + len('</nav>')
    header_part = content[:nav_end]
    
    # Change <title>
    header_part = re.sub(r'<title>.*?</title>', '<title>Contact Us - Mindtree Nursing Solutions</title>', header_part)
    
    # Add contact.css
    header_part = header_part.replace('<link rel="stylesheet" href="css/index.css">', '<link rel="stylesheet" href="css/contact.css">')
    
    # Ensure contact link is active
    header_part = header_part.replace('<li><a href="index" class="active">Home</a></li>', '<li><a href="index.html">Home</a></li>')
    header_part = header_part.replace('<li><a href="contact.html">Contact Us</a></li>', '<li><a href="contact.html" class="active">Contact Us</a></li>')

    # Extract the footer part
    # from <!-- Fixed Action Buttons --> onwards (or whatever is the standard footer)
    footer_start = content.find('<!-- Fixed Action Buttons -->')
    footer_part = content[footer_start:]
    
    # Remove index-specific modals from footer part if they are in there.
    # We removed contact modal, so it's fine.
    
    contact_section = """
    <!-- Page Header -->
    <section class="page-header">
        <div class="container">
            <h1>Contact Us</h1>
            <p>Get in touch with our training centers and offices across the globe.</p>
        </div>
    </section>

    <!-- Contact Cards Section -->
    <section class="contact-section">
        <div class="container">
            <div class="contact-grid">
                
                <!-- NEW ZEALAND -->
                <div class="contact-card">
                    <div class="card-icon"><i class="fas fa-map-marker-alt"></i></div>
                    <h3>NEW ZEALAND</h3>
                    <p>30/167 Whitney Street, Blockhouse Bay,<br>Auckland, 0600</p>
                    <div class="contact-details">
                        <a href="tel:+64212178770"><i class="fas fa-phone"></i> +64 212178770</a>
                        <a href="mailto:info@mindtreenursing.com"><i class="fas fa-envelope"></i> info@mindtreenursing.com</a>
                    </div>
                    <a href="https://maps.google.com/?q=30/167+Whitney+Street,+Blockhouse+Bay,+Auckland" target="_blank" class="map-link">View map <i class="fas fa-arrow-right"></i></a>
                </div>

                <!-- AUSTRALIA -->
                <div class="contact-card">
                    <div class="card-icon"><i class="fas fa-map-marker-alt"></i></div>
                    <h3>AUSTRALIA</h3>
                    <p>22/2 Antis Street Canberra,<br>ACT</p>
                    <div class="contact-details">
                        <a href="tel:+61493669557"><i class="fas fa-phone"></i> +61 493669557</a>
                        <a href="mailto:info@mindtreenursing.com"><i class="fas fa-envelope"></i> info@mindtreenursing.com</a>
                    </div>
                    <a href="https://maps.google.com/?q=22/2+Antis+Street+Canberra,+ACT" target="_blank" class="map-link">View map <i class="fas fa-arrow-right"></i></a>
                </div>

                <!-- INDIA -->
                <div class="contact-card">
                    <div class="card-icon"><i class="fas fa-map-marker-alt"></i></div>
                    <h3>INDIA</h3>
                    <p>Olivet, M.C Road, Panavely<br>Kottarakkara, Kollam, Kerala 691532</p>
                    <div class="contact-details">
                        <a href="tel:+918075301169"><i class="fas fa-phone"></i> +91 8075301169</a><br>
                        <a href="tel:+917306724695"><i class="fas fa-phone"></i> +91 7306724695</a>
                        <a href="mailto:info@mindtreenursing.com"><i class="fas fa-envelope"></i> info@mindtreenursing.com</a>
                    </div>
                    <a href="https://maps.google.com/?q=Olivet,+M.C+Road,+Panavely,+Kottarakkara" target="_blank" class="map-link">View map <i class="fas fa-arrow-right"></i></a>
                </div>

                <!-- OSCE Training in Christchurch -->
                <div class="contact-card highlight-card">
                    <div class="card-icon"><i class="fas fa-user-nurse"></i></div>
                    <h3>OSCE Training in Christchurch</h3>
                    <p>110 Sir John McKenzie Avenue,<br>Christchurch</p>
                    <div class="contact-details">
                        <a href="tel:+64221230023"><i class="fas fa-phone"></i> +64 221230023</a>
                        <a href="mailto:info@mindtreenursing.com"><i class="fas fa-envelope"></i> info@mindtreenursing.com</a>
                    </div>
                    <a href="https://maps.google.com/?q=110+Sir+John+McKenzie+Avenue,+Christchurch" target="_blank" class="map-link">View map <i class="fas fa-arrow-right"></i></a>
                </div>

                <!-- OSCE Training in Auckland -->
                <div class="contact-card highlight-card">
                    <div class="card-icon"><i class="fas fa-user-nurse"></i></div>
                    <h3>OSCE Training in Auckland</h3>
                    <p>81A Tiverton Road, Blockhouse Bay,<br>Auckland, 0600</p>
                    <div class="contact-details">
                        <a href="tel:+64221230023"><i class="fas fa-phone"></i> +64 221230023</a>
                        <a href="mailto:info@mindtreenursing.com"><i class="fas fa-envelope"></i> info@mindtreenursing.com</a>
                    </div>
                    <a href="https://maps.google.com/?q=81A+Tiverton+Road,+Blockhouse+Bay,+Auckland" target="_blank" class="map-link">View map <i class="fas fa-arrow-right"></i></a>
                </div>

                <!-- OSCE Training in Kerala -->
                <div class="contact-card highlight-card">
                    <div class="card-icon"><i class="fas fa-user-nurse"></i></div>
                    <h3>OSCE Training in Kerala</h3>
                    <p>Olivet, M.C. Road, Panavely,<br>Kottarakkara, Kollam, Kerala 691532</p>
                    <div class="contact-details">
                        <a href="tel:+919778286707"><i class="fas fa-phone"></i> +91 9778286707</a>
                        <a href="mailto:info@mindtreenursing.com"><i class="fas fa-envelope"></i> info@mindtreenursing.com</a>
                    </div>
                    <a href="https://maps.google.com/?q=Olivet,+M.C.+Road,+Panavely,+Kottarakkara" target="_blank" class="map-link">View map <i class="fas fa-arrow-right"></i></a>
                </div>

            </div>
        </div>
    </section>
    """

    final_html = header_part + contact_section + footer_part
    
    with open('d:/editable web/contact.html', 'w', encoding='utf-8') as f:
        f.write(final_html)

if __name__ == "__main__":
    create_contact_page()
