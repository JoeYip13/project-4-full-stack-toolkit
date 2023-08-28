# Testing

<figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693232802/Readme/Am-I-Responsive/am-i-responsive-tasty-tales_vuk0il.jpg"
        alt="Tasty tales website through Am i responsive screenshot">
        <figcaption>Tasty Tales Am I Responsive</figcaption>
</figure>

---
## Table of Contents

1. [Automated Testing](#Automated-testing)
2. [W3C Validator](#w3c-validator)
3. [PEP8 Validator](#pep8-validator)
4. [Responsive Design](#responsive)
5. [Lighthouse Testing](#lighthouse-testing)
6. [PageSpeed Insights](#pagespeed-insights)
6. <details open><summary><a href="#manual-testing">Manual Testing</a></summary>

    - [Navigation Bar](#navigation-bar)
    - [Footer](#footer)
    - [Home Page](#home-page)
    - [Blog Post Detail view](#blog-post-detail-view)
    - [About Page](#about-page)
    - [Contact Page](#contact-page)
    - [Sign Up Page](#sign-up-page)
    - [Login Page](#login-page)
    - [Administration](#administration)
    - [More Manual Scenario Base Testing](#more-manual-scenario-base-testing)
   </details>
7. [Bugs](#bugs)

---

## Automated Testing
---
## W3C Validator
<details>
<summary>W3C Validator</summary>
<figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693231384/Testing/W3C%20Validation/w3c-validation_qwyqak.png"
        alt="W3C validator">
        <figcaption>W3C Validator</figcaption>
</figure>
</details>
<details>
<summary>W3C CSS Validator</summary>
<figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693231384/Testing/W3C%20Validation/w3c-css-validation_czyeju.png">
        <figcaption>W3C CSS Validator</figcaption>
</figure>
</details>

---
## PEP8 Validator
Code Institute [CI Python Linter](https://pep8ci.herokuapp.com/) was used to validate all python files.

#### Tasty Tales Project
<details>
    <summary>asgi.py - No errors</summary>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693166646/Testing/PEP8%20Python%20Linter/asgi.py_dnselc.png"
        alt="python linter asgi.py file">
        <figcaption>Tasty Tales asgi.py</figcaption>
</figure>
</details>
<details>
    <summary>settings.py - No errrors, except line too long</summary>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693166647/Testing/PEP8%20Python%20Linter/settings.py_yftury.png"
        alt="python linter settings file">
        <figcaption>Tasty Tales settings.py</figcaption>
</figure>
</details>
<details>
    <summary>urls.py - No errors</summary>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693166647/Testing/PEP8%20Python%20Linter/tasty-tales-urls.py_mogfbc.png"
        alt="python linter urls.py file">
        <figcaption>Tasty Tales urls.py</figcaption>
</figure>
</details>
<details>
    <summary>wsgi.py - No errors</summary>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693166647/Testing/PEP8%20Python%20Linter/wsgi.py_kmkf5u.png"
        alt="python linter wsgi.py file ">
        <figcaption>Tasty Tales wsgi.py</figcaption>
    </figure>
</details>

#### Food Blog App
<details>
    <summary>admin.py - No errors</summary>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693166646/Testing/PEP8%20Python%20Linter/food-blog-admin.py_jdunft.png"
        alt="python linter admin.py file">
        <figcaption>Food Blog admin.py</figcaption>
</figure>
</details>
<details>
    <summary>apps.py - No errors</summary>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693166646/Testing/PEP8%20Python%20Linter/food-blog-apps.py_sjycys.png"
        alt="python linter apps.py file">
        <figcaption>Food Blog apps.py</figcaption>
</figure>
</details>
<details>
    <summary>forms.py - No errors</summary>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693166647/Testing/PEP8%20Python%20Linter/food-blog-forms.py_dcagnx.png"
        alt="python linter forms.py file">
        <figcaption>Food Blog forms.py</figcaption>
</figure>
</details>
<details>
    <summary>models.py - No errors</summary>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693166646/Testing/PEP8%20Python%20Linter/food-blog-models.py_fim9t7.png"
        alt="python linter models.py file">
        <figcaption>Food Blog models.py</figcaption>
</figure>
</details>
<details>
    <summary>urls.py - No errors</summary>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693166647/Testing/PEP8%20Python%20Linter/food-blog-urls.py_txddst.png"
        alt="python linter urls.py file">
        <figcaption>Food Blog urls.py</figcaption>
</figure>
</details>
<details>
    <summary>views.py - No errors</summary>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693166647/Testing/PEP8%20Python%20Linter/food-blog-views.py_wgieqj.png"
        alt="python linter views.py file">
        <figcaption>Food Blog views.py</figcaption>
</figure>
</details>

#### About App

<details>
    <summary>admin.py - No errors</summary>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693166646/Testing/PEP8%20Python%20Linter/about-admin.py_kziykd.png"
        alt="python linter admin.py file">
        <figcaption>About admin.py</figcaption>
</figure>
</details>
<details>
    <summary>apps.py - No errors</summary>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693166646/Testing/PEP8%20Python%20Linter/about-apps.py_u00njr.png"
        alt="python linter apps.py">
        <figcaption>About apps.py</figcaption>
</figure>
</details>
<details>
    <summary>forms.py - No errors</summary>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693166646/Testing/PEP8%20Python%20Linter/about-forms.py_lvwnab.png"
        alt="python linter forms.py file ">
        <figcaption>About forms.py</figcaption>
</figure>
</details>
<details>
    <summary>models.py - No errors</summary>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693166646/Testing/PEP8%20Python%20Linter/about-models.py_sz7bc1.png"
        alt="python linter models.py file">
        <figcaption>About models.py</figcaption>
</figure>
</details>
<details>
    <summary>urls.py - No errors</summary>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693166646/Testing/PEP8%20Python%20Linter/about-urls.py_ajt29r.png"
        alt="python linter urls.py file">
        <figcaption>About urls.py</figcaption>
</figure>
</details>
<details>
    <summary>views.py - No errors</summary>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693166646/Testing/PEP8%20Python%20Linter/about-views.py_dk4kn4.png"
        alt="python linter views.py file">
        <figcaption>About views.py</figcaption>
</figure>
</details>

---
## Responsive

<details>
<summary>Mobile view</summary>
<figure align="">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693221546/Testing/Responsive/mobile/mobile-screen-size-home_gr0vnm.png" width="200"
        alt="Tasty tales mobile view">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693221545/Testing/Responsive/mobile/mobile-screen-size-about_vwggpe.png" width="200"
        alt="Tasty tales mobile view">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693221546/Testing/Responsive/mobile/mobile-screen-size-contact_l27e3p.png" width="200"
        alt="Tasty tales mobile view">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693221547/Testing/Responsive/mobile/mobile-screen-size-signup_h4o61k.png" width="200"
        alt="Tasty tales mobile view">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693221546/Testing/Responsive/mobile/mobile-screen-size-login_f3us1z.png" width="200"
        alt="Tasty tales mobile view">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693221547/Testing/Responsive/mobile/mobile-screen-size-nav_rakues.png" width="200"
        alt="Tasty tales mobile view">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693221545/Testing/Responsive/mobile/mobile-screen-size-blog-post_dwigoq.png" width="200"
        alt="Tasty tales mobile view">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693221547/Testing/Responsive/mobile/mobile-screen-size-own-post_h1hcnm.png" width="200"
        alt="Tasty tales mobile view">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693221547/Testing/Responsive/mobile/mobile-screen-size-update-post_t2k6xv.png" width="200"
        alt="Tasty tales mobile view">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693221545/Testing/Responsive/mobile/mobile-screen-size-comments_a3v131.png" width="200"
        alt="Tasty tales mobile view">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693221545/Testing/Responsive/mobile/mobile-screen-size-delete-comment_dvsamc.png" width="200"
        alt="Tasty tales mobile view">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693221545/Testing/Responsive/mobile/mobile-screen-size-add-post_ycto5t.png" width="200"
        alt="Tasty tales mobile view">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693221545/Testing/Responsive/mobile/mobile-screen-size-delete-post-confirm_zhvmla.png" width="200"
        alt="Tasty tales mobile view">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693221546/Testing/Responsive/mobile/mobile-screen-size-delete-post_gh8z9w.png" width="200"
        alt="Tasty tales mobile view">
        <figcaption>Mobile view</figcaption>
</figure>
</details>

<details>
    <summary>Tablet view</summary>
    <figure align="">
        <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693221548/Testing/Responsive/tablet/tablet-screen-size_j4bijo.png" width="200"
            alt="Tasty tales tablet view">
        <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693221548/Testing/Responsive/tablet/tablet-screen-size-food_w75lx1.png" width="200"
            alt="Tasty tales tablet view">
        <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693221548/Testing/Responsive/tablet/tablet-screen-size-update_o6vtoe.png" width="200"
            alt="Tasty tales tablet view">
        <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693221548/Testing/Responsive/tablet/tablet-screen-size-own-post_hp3n3i.png" width="200"
            alt="Tasty tales tablet view">
        <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693221548/Testing/Responsive/tablet/tablet-screen-size-contact_zcyuuq.png" width="200"
            alt="Tasty tales tablet view">
        <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693221548/Testing/Responsive/tablet/tablet-screen-size-delete-post_bz63mp.png" width="200"
            alt="Tasty tales tablet view">
        <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693221548/Testing/Responsive/tablet/tablet-screen-size-delete-post-confirm_hpwtxh.png" width="200"
            alt="Tasty tales tablet view">
        <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693221547/Testing/Responsive/tablet/tablet-screen-size-about_zmiq39.png" width="200"
            alt="Tasty tales tablet view">
        <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693221547/Testing/Responsive/tablet/tablet-screen-size-blog-post_cl8apu.png" width="200"
            alt="Tasty tales tablet view">
        <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693221547/Testing/Responsive/tablet/tablet-screen-size-comments_inp7mg.png" width="200"
            alt="Tasty tales tablet view">
        <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693221547/Testing/Responsive/tablet/tablet-screen-size-add-post_p5g2tf.png" width="200"
            alt="Tasty tales tablet view">
        <figcaption>Tablet view</figcaption>
    </figure>
</details>

<details>
    <summary>Laptop view</summary>
    <figure align="">
        <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693221547/Testing/Responsive/laptop/large-screen-size_yia6yj.png" width="200"
            alt="Tasty tales laptop view">
        <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693221547/Testing/Responsive/laptop/large-screen-size-food_flmvcl.png" width="200"
            alt="Tasty tales laptop view">
        <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693221546/Testing/Responsive/laptop/large-screen-size-contact_xnxzz8.png" width="200"
            alt="Tasty tales laptop view">
        <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693221546/Testing/Responsive/laptop/laptop-screen-size-home_dpflfz.png" width="200"
            alt="Tasty tales laptop view">
        <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693221546/Testing/Responsive/laptop/laptop-screen-size-blog-post_flxgoa.png" width="200"
            alt="Tasty tales laptop view">
        <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693221545/Testing/Responsive/laptop/laptop-screen-size-about_tqzgqn.png" width="200"
            alt="Tasty tales laptop view">
        <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693221545/Testing/Responsive/laptop/large-screen-size-update-post_qojulj.png" width="200"
            alt="Tasty tales laptop view">
        <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693221545/Testing/Responsive/laptop/laptop-screen-size-comments_r8gufu.png" width="200"
            alt="Tasty tales laptop view">
        <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693221545/Testing/Responsive/laptop/large-screen-size-delete-post-confirm_g0zrfv.png" width="200"
            alt="Tasty tales laptop view">
        <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693221545/Testing/Responsive/laptop/large-screen-size-delete-post_cobmme.png" width="200"
            alt="Tasty tales laptop view">
        <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693221545/Testing/Responsive/laptop/large-screen-size-add-post_iypi6z.png" width="200"
            alt="Tasty tales laptop view">
        <figcaption>Laptop view</figcaption>
    </figure>
</details>

---
## PageSpeed Insights
<details>
    <summary>Home Page</summary>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693231678/Testing/Pagespeed/homepage_m2pfs5.png"
        alt="Home page pagespeed insights">
    <figcaption>Home page pagespeed insights</figcaption>
    </figure>
</details>
<details>
    <summary>About Page</summary>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693231678/Testing/Pagespeed/about-page_y3a90x.png" 
        alt="About page pagespeed insights">
    <figcaption>About page pagespeed insights </figcaption>
    </figure>
</details>
<details>
    <summary>Contact Page</summary>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693231678/Testing/Pagespeed/contact-page_czmauf.png" 
        alt="Contact page pagespeed insights">
    <figcaption>Contact page pagespeed insights</figcaption>
    </figure>
</details>
<details>
    <summary>Sign Up Page</summary>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693231679/Testing/Pagespeed/signup-page_vhlz1z.png"
        alt="Sign up page pagespeed insights">
    <figcaption>Sign up page pagespeed insights</figcaption>
    </figure>
</details>
<details>
    <summary>Login Page</summary>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693231679/Testing/Pagespeed/login-page_t5zrqg.png"
        alt="Login page pagespeed insights">
    <figcaption>Login page pagespeed insights</figcaption>
    </figure>
</details>
<details>
    <summary>Blog Post Detail View Page</summary>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693231678/Testing/Pagespeed/blog-post-page_axdmek.png"
        alt="Blog post detail view page">
    <figcaption>Blog post detail view page</figcaption>
    </figure>
</details>

---

## Lighthouse Testing
<details>
    <summary>Add Post Page</summary>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693231674/Testing/Lighthouse/add-post-page_bxgbcl.png"
        alt="Add post page lighthouse">
    <figcaption>Add post page lighthouse</figcaption>
    </figure>
</details>
<details>
    <summary>Update Post Page</summary>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693231674/Testing/Lighthouse/update-post-page_ynytyq.png"
        alt="Update post page lighthouse">
    <figcaption>Update post page lighthouse</figcaption>
    </figure>
</details>
<details>
    <summary>Delete Post Page</summary>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693231673/Testing/Lighthouse/delete-post-page_dflnul.png"
        alt="Delete page lighthouse">
    <figcaption>Delete post page lighthouse</figcaption>
    </figure>
</details>
<details>
    <summary>Log out Page</summary>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693231673/Testing/Lighthouse/sign-out-page_nf04pi.png"
        alt="Log out page lighthouse">
    <figcaption>Log out page lighthouse</figcaption>
    </figure>
</details>

---
## Manual Testing
### Navigation Bar
| Feature | Action | Expected Result | PASS/FAIL |
| ------- | ------ | --------------- | --------- |
| Website Logo | Display | Website logo is displayed when on homepage | PASS |
| Navbar | Display | When user is not logged in only links to Food, About, Contact, Sign up, Login should be displayed | PASS |
| Navbar | Hover | On mouse hover can see the hover effect of a underline over the links | PASS |
| Navbar | Display | When user is logged in only links to Food, About, Contact, User's display name with a Profile Icon and a dropdown arrow menu. | PASS |
| Profile dropdown | Click | When a user is logged in and clicks on the profile icon or dropdown arrow menu. It should display a Add Post link and Logout link | PASS |
| Profile dropdown | Click | When a user is logged in and clicks on the Add post link it should open Add post page | PASS |
| Profile dropdown | Click | When a user is logged in and clicks on the logout link is should open to logout page | PASS |
| Navbar | Click | "Food" link should open home page | PASS |
| Navbar | Click | "About" link should open About page | PASS |
| Navbar | Click | "Contact" link should open Contact page  | PASS |
| Navbar | Click | "Sign Up" should open sign up page | PASS |
| Navbar | Click | "Login" should open log in page | PASS |
| Website Logo | Click | Website logo link should open home page | PASS |

<details><summary>Navbar Testing</summary>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693236060/Testing/Navigation%20testing/navbar-food_djskzj.png"
        alt="testing hover effect on mouse over">
    <figcaption>Testing hover effect on mouse over</figcaption>
    </figure>
</details>

### Footer
| Feature | Action | Expected Result | PASS/FAIL |
| ------- | ------ | --------------- | --------- |
| Footer | Display | Should only be visible at the bottom of the webpage | PASS |
| Footer Navbar | Display | Should display a secondary navbar with only links to Food, About, Contact | PASS |
| Footer Social Media | Display | Should display social media links in the footer section | PASS |
| Navbar | Hover | On mouse hover can see the hover effect of a underline over the links | PASS |
| Footer Social Media | Hover | On mouse hover can see the hover effect of the social media icons | PASS |
| Footer Navbar | Click | "Food" link should open to home page | PASS |
| Footer Navbar | Click | "About" link should open About page | PASS |
| Footer Navbar | Click | "Contact" link should open Contact page | PASS |
| Footer Navbar | Click | Social media links should open a blank page to each their social media pages | PASS |

<details><summary>Footer Testing</summary>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693133130/Readme/Main%20UX/footer-nav-links_nuujki.jpg"
        alt="testing hover effect on mouse over">
    <figcaption>Testing hover effect on mouse over</figcaption>
    </figure>
    <br>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693133130/Readme/Main%20UX/footer-social-links_hnsfo2.jpg"
        alt="testing hover effect on mouse over">
    <figcaption>Testing hover effect on mouse over</figcaption>
    </figure>
</details>

### Home Page
| Feature | Action | Expected Result | PASS/FAIL |
| ------- | ------ | --------------- | --------- |
| Homepage | Display | Homepage is displayed when url is passed through into the browser | PASS |
| Feature Carousel | Display | Should display a feature carousel in the hero section of the page | PASS |
| Feature Carousel | Display | Should display a slide indicators | PASS |
| List of Blog Posts | Display | Should display a list of blog posts below the hero section of the page | PASS |
| Add Post Link | Display | When a user is logged in a Add Post button should be displayed on the main home page | PASS |
| Blog Posts | Hover | When a user hovers over a blog post title or excerpt, it should change color to indicate a link | PASS |
| Feature Carousel | Click | When a user clicks on the slide indicators on the carousel, it should be responsive to slide to which ever direction a user has requested | PASS |
| Add Post Link | Click | Should open a Add Post page | PASS |
| Blog Posts | Click | When a user clicks on a blog post title or excerpt, it should open that blog post in a detail view | PASS |

<details><summary>Home Page Testing</summary>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693238364/Readme/Main%20UX/hover-effect-over-blog-post_kjyy2w.png"
        alt="testing hover effect on mouse over">
    <figcaption>Testing hover effect on mouse over</figcaption>
    </figure>
</details>

### Blog Post Detail View
| Feature | Action | Expected Result | PASS/FAIL |
| ------- | ------ | --------------- | --------- |
| Blog Post | Display | Blog post is display when url is passed through into the browser | PASS |
| Blog Post | Display | Blog post should display the image and content of the blog post | PASS |
| Comment | Display | Comment section is displayed below the content | PASS |
| Comment Form | Display | When a user is not logged in the comment form should display a message to sign up to leave a comment | PASS |
| Comment Form | Display | When a user is not logged in the comment form should display link to sign up | PASS |
| Comment Form | Display | When a user is logged in a comment form is displayed with their username displayed in the form and a text area input with a submit button   | PASS |
| Comment | Input | A user logged in can input data in the text field | PASS |
| Comment | Click | A user logged in can submit data passed in the text field | PASS |
| Comment | Click | When a user logged in has not input any data in the text field, a error message should appear | PASS |

<details><summary>Blog Post Testing</summary>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693136186/Readme/Main%20UX/food-blog-post-detail-view_ebi6yh.jpg"
        alt="display blog post testing">
    <figcaption>Display Blog Post</figcaption>
    </figure>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693238949/Testing/blog%20post%20testing/comment-section-new-user_oa3fr4.png"
        alt="comment section as new user">
    <figcaption>Comment view as new user</figcaption>
    </figure>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693238947/Testing/blog%20post%20testing/comment-section-logged-in_gjrzcg.png">
    <figcaption>Comment view as a logged in user</figcaption>
    </figure>
</details>

### About Page
| Feature | Action | Expected Result | PASS/FAIL |
| ------- | ------ | --------------- | --------- |
| About Page | Display | About page is dispayed when url is passed through into the browser | PASS |
| About content | Display | Should display content of About in the hero section of the page | PASS |

### Contact Page
| Feature | Action | Expected Result | PASS/FAIL |
| ------- | ------ | --------------- | --------- |
| Contact Page | Display | Contact page is dispayed when url is passed through into the browser | PASS |
| Contact information | Display | Should display contact information on the page | PASS |
| Contact Form | Display | Contact form is dispayed on the page with name, email, subject and message | PASS |
| Contact Form | Input | A user can input their data in the name, email, subject and message text area | PASS |
| Contact Form | Click | When a user has inputted all data fields, they can submit their data by clicking the send message button | PASS |
| Contact Form | Click | When a user has not input any data in the required fields, a error message should appear | PASS |

<details><summary>Contact Testing</summary>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693239286/Testing/Contact%20form%20testing/contact-form-test_e9duqo.jpg">
    <figcaption>Contact form testing</figcaption>
    </figure>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693239286/Testing/Contact%20form%20testing/contact-form-test-no-input-feedback_clizjb.jpg"
        alt="contact form error message">
    <figcaption>Contact form error message</figcaption>
    </figure>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693239286/Testing/Contact%20form%20testing/contact-form-test-success-feedback_czlenf.jpg"
        alt="contact form sent success alert">
    <figcaption>Contact form sent success alert</figcaption>
    </figure>
</details>

### Sign Up Page
| Feature | Action | Expected Result | PASS/FAIL |
| ------- | ------ | --------------- | --------- |
| Sign Up Page | Display | Sign Up page is dispayed when url is passed through into the browser | PASS |
| Sign Up Page | Display | Display content if a user is already signed up and a link to login page | PASS |
| Sign Up Form | Display | Should display a sign up form on the page with inout fields username, email, password, password again | PASS |
| Sign Up Form | Input | A user can input their data in the name, email, password and password again area | PASS |
| Sign Up Form | Click | When a user has inputted all data fields, they can submit their data by clicking the Sign Up button | PASS |
| Sign Up Form | Click | When a user has not input any data in the required fields, a error message should appear | PASS |

<details><summary>Sign Up Testing</summary>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693235222/Testing/New%20user%20testing/sign-up-new-user-test_lyv1tk.jpg"
        alt="Sign up new user testing">
    <figcaption>Sign up new user testing</figcaption>
    </figure>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693235222/Testing/New%20user%20testing/sign-up-all-auth_acxgw0.jpg"
        alt="Sign up new user already exists testing">
    <figcaption>If user already exists testing</figcaption>
    </figure>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693235222/Testing/New%20user%20testing/sign-up-success-feedback_zh0d4w.jpg"
        alt="New user success alert">
    <figcaption>New user success alert</figcaption>
    </figure>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693235222/Testing/New%20user%20testing/test-user-logout_olg8vb.jpg"
        alt="Shows user name in nav bar">
    <figcaption>Shows user name in the nav bar</figcaption>
    </figure>
</details>

### Login Page
| Feature | Action | Expected Result | PASS/FAIL |
| ------- | ------ | --------------- | --------- |
| Login Page | Display | Login page is dispayed when url is passed through into the browser | PASS |
| Login Page | Display | Display content if a user is not a signed up, a link to sign up page | PASS |
| Login Form | Display | Should display a log in form on the page with inout fields username, password, sign in button | PASS |
| Login Form | Input | A user can input their data in the username and password area | PASS |
| Login Form | Click | When a user has inputted all data fields, they can submit their data by clicking the Sign Up button | PASS |
| Login Form | Click | When a user has not input any data in the required fields, a error message should appear | PASS |
| Login Form | Click | When a user has not input any data in the required fields, a error message should appear | PASS |

<details><summary>Login Testing</summary>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693237338/Testing/Login%20testing/login-testing_qycrtd.png"
        alt="sign in">
    <figcaption>Sign In</figcaption>
    </figure>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693237338/Testing/Login%20testing/login-testing-success_kakawe.png"
        alt="sign in success">
    <figcaption>Sign in success alert</figcaption>
    </figure>
</details>

### Administration
| Feature | Action | Expected Result | PASS/FAIL |
| ------- | ------ | --------------- | --------- |
| Admin | Display | As a site admin the admim page is displayed when url is passed through into the browser | PASS |
| Admin About | Display | As a site admin the admim about displays all the information in the website for the about page, About, Contact messages and Contact  | PASS |
| Admin Users | Display | As a site admin I can see the Users signed up on the website | PASS |
| Admin Food Blog | Display | As a site admin I can see the Food Blog posted on the website. Comments and Posts | PASS |
| Admin About | Click | As a admin clicking the About brings me the About information for the website  | PASS |
| Admin About | Click | As a admin I can choose a new file to upload to display in the about page | PASS |
| Admin About | Input | As a admin I can input a new title for the about page and change the content. | PASS |
| Admin About | Click | As a admin I can save new data in the about section. | PASS |
| Admin Contact Messages | Display | As a admin I can see a list of users who have submitted a contact form on the website | PASS |
| Admin Contact Messages | Display | As a admin I can see the users contact information to return a message back to the user | PASS |
| Admin Contact | Click | As a admin clicking the Contact brings me the Contact information for the website | PASS |
| Admin Contact | Input | As a admin I can input a new title for the contact page and change the content | PASS |
| Admin Contact | Input | As a admin I can input a new email and contact number for the contact page. | PASS |
| Admin Contact | Click | As a admin I can save new data in the contact section. | PASS |
<details><summary>Administration Testing</summary>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693239858/Testing/Admin/admin-view_pxlwjg.png"
        alt="admin view">
    <figcaption>Admin view</figcaption>
    </figure>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693239858/Testing/Admin/admin-about_e5e70k.png"
        alt="Admin about view">
    <figcaption>Admin Contact</figcaption>
    </figure><figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693239858/Testing/Admin/admin-contacts_jhkvww.png"
        alt="admin contact view">
    <figcaption>Admin Contact</figcaption>
    </figure>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693239858/Testing/Admin/admin-users_dgasji.png"
        alt="admin users view">
    <figcaption>Admin Users</figcaption>
    </figure>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693239858/Testing/Admin/admin-food-blog-comments_xecvgx.png"
        alt="admin comments view">
    <figcaption>Admin Comments</figcaption>
    </figure>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693239858/Testing/Admin/admin-food-blog-posts_kmzupd.png"
        alt="admin posts view">
    <figcaption>Admin Posts</figcaption>
    </figure>
</details>

---
## More Manual Scenario Base Testing
### Posting a Comment
| | PASS/FAIL |
| ------- | ------ |
| As a user or admin I can post a comment on a blog post | PASS |
| As a user or admin I can see my comment on a blog post | PASS |
| As a user or admin I can edit my comment on a blog post | PASS |
| As a user or admin I can delete my comment on a blog post | PASS |
| As a admin I can approve any comments on a blog post | PASS |
| As a admin I can un-approve any comments on a blog post | PASS |
| As a admin I can delete any comments on a blog post | PASS |
<details><summary>Posting a comment testing</summary>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693240767/Testing/Comment%20testing/post-comment-test_vxeaf3.jpg"
        alt="comment testing">
    <figcaption>Comment testing</figcaption>
    </figure>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693240767/Testing/Comment%20testing/comment-post-success-feedback_yopya2.jpg"
        alt="comment testing">
    <figcaption>Comment success testing</figcaption>
    </figure>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693240767/Testing/Comment%20testing/post-comment-test-awaiting-approval_g1jcks.jpg"
        alt="comment testing">
    <figcaption>Comment awaiting approval testing</figcaption>
    </figure>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693240767/Testing/Comment%20testing/comment-edit_uguwav.jpg"
        alt="comment testing">
    <figcaption>Comment edit testing</figcaption>
    </figure>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693240767/Testing/Comment%20testing/comment-edit-update-success_bhx9hr.jpg"
        alt="comment testing">
    <figcaption>Comment edit success testing</figcaption>
    </figure>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693240767/Testing/Comment%20testing/delete-comment_vkhfn4.jpg"
        alt="comment testing">
    <figcaption>Comment delete testing</figcaption>
    </figure>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693240768/Testing/Comment%20testing/comment-delete-feedback_qsvqey.jpg"
        alt="comment testing">
    <figcaption>Comment delete success testing</figcaption>
    </figure> 
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693240767/Testing/Comment%20testing/comment-delete-view_nmxs8y.jpg"
        alt="comment testing">
    <figcaption>Comment deleted comment view</figcaption>
    </figure>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693240767/Testing/Comment%20testing/comment-admin-view_zebkt9.jpg"
        alt="comment testing">
    <figcaption>Comment approve by Admin testing</figcaption>
    </figure>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693240768/Testing/Comment%20testing/comment-admin-approve_hy9aj6.jpg"
        alt="comment testing">
    <figcaption>Comment approved by Admin testing</figcaption>
    </figure>
</details>

### Adding a new Blog Post
| | PASS/FAIL |
| ------- | ------ |
| As a logged in user or admin I can add a new blog post | PASS |
| As a logged in user or admin I can see my approved blog post | PASS |
| As a logged in user or admin I can edit my blog post | PASS |
| As a logged in user or admin I can delete my blog post | PASS |
| As a admin I can approve any blog post | PASS |
| As a admin I can un-approve any blog post | PASS |
| As a admin I can delete any blog post | PASS |
<details><summary>Adding a new Blog Post testing</summary>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693241728/Testing/Add%20post%20testing/add-post_pvso4j.jpg"
        alt="Adding a blog post testing">
    <figcaption>Add Blog post testing</figcaption>
    </figure>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693241728/Testing/Add%20post%20testing/test-post_za9m22.jpg"
        alt="Adding a blog post testing">
    <figcaption>Add Blog post testing</figcaption>
    </figure>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693241728/Testing/Add%20post%20testing/test-post-success-feedback_jjccsh.jpg"
        alt="Adding a blog post testing">
    <figcaption>Add Blog post testing</figcaption>
    </figure>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693241728/Testing/Add%20post%20testing/test-post-admin-panel_syonem.jpg"
        alt="Adding a blog post testing">
    <figcaption>Add Blog post Admin authorization view testing</figcaption>
    </figure>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693241728/Testing/Add%20post%20testing/test-post-admin-panel-authorization_d591w7.jpg"
        alt="Adding a blog post testing">
    <figcaption>Add Blog post Admin authorization draft to published testing</figcaption>
    </figure>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693241728/Testing/Add%20post%20testing/test-post-admin-published_xb5rkj.jpg"
        alt="Adding a blog post testing">
    <figcaption>Add Blog admin authorized published</figcaption>
    </figure>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693241728/Testing/Add%20post%20testing/test-post-success_oiocoq.jpg"
        alt="Adding a blog post testing">
    <figcaption>Blog Post Admin Authorized</figcaption>
    </figure>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693241728/Testing/Add%20post%20testing/test-post-detail-view_lxhsqu.jpg"
        alt="Adding a blog post testing">
    <figcaption>Add Blog post detail view</figcaption>
    </figure>
</details>

### Updating a Blog Post
| | PASS/FAIL |
| ------- | ------ |
| As a logged in user or admin I can update my blog post | PASS |
| As a logged in user or admin I can see my updated blog post | PASS |
| As a logged in user or admin I can delete my blog post | PASS |
<details><summary>Updating a Blog Post testing</summary>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693241748/Testing/Update%20post%20testing/test-post-update-post-view_mogqvo.jpg"
        alt="Updating a blog post testing">
    <figcaption>Updating a Blog post testing</figcaption>
    </figure>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693241748/Testing/Update%20post%20testing/test-post-input_ftxxzj.jpg"
        alt="Updating a blog post testing">
    <figcaption>Updating a Blog post with new input testing</figcaption>
    </figure>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693241748/Testing/Update%20post%20testing/test-post-update-success_vlsjgh.jpg"
        alt="Updating a blog post testing">
    <figcaption>Updating a Blog post success alert testing</figcaption>
    </figure>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693241749/Testing/Update%20post%20testing/test-post-admin-panel-update-success_rol6uy.jpg"
        alt="Updating a blog post testing">
    <figcaption>Updating a Blog admin view</figcaption>
    </figure>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693241748/Testing/Update%20post%20testing/test-post-update-post-view-success_innvri.jpg"
        alt="Updating a blog post testing">
    <figcaption>Updatied blog post detail view</figcaption>
    </figure>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693241749/Testing/Update%20post%20testing/test-post-update-success-landing-page_i5xcay.jpg"
        alt="Updating a blog post testing">
    <figcaption>Updated Blog post testing</figcaption>
    </figure>
</details>

### Deleting a Blog Post
| | PASS/FAIL |
| ------- | ------ |
| As a logged in user or admin I can delete my blog post | PASS |
| As a logged in user or admin I can no longer see my deleted blog post anywhere on the website | PASS |
| As a user or admin my deleted blog post should be removed from the database | PASS |
<details><summary>Deleting a Blog Post testing</summary>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693241735/Testing/Delete%20post%20testing/test-post-delete_wujvqk.jpg"
        alt="Deleting a blog post testing">
    <figcaption>Deleting a Blog post testing</figcaption>
    </figure>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693241735/Testing/Delete%20post%20testing/test-post-delete-confirmation_fxw0tk.jpg"
        alt="Deleting a blog post testing">
    <figcaption>Deleting a Blog post confirm delete testing</figcaption>
    </figure>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693241735/Testing/Delete%20post%20testing/test-post-delete-success-feedback_qcyh4s.jpg"
        alt="Deleting a blog post testing">
    <figcaption>Deleting a Blog post testing</figcaption>
    </figure>
    <figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693241735/Testing/Delete%20post%20testing/test-post-delete-admin-panel_xvxynk.jpg"
        alt="Deleting a blog post testing">
    <figcaption>Deleted Blog post admin view testing</figcaption>
    </figure>
</details>

---
## Bugs
### Fixed Bugs
- Installing whitenoise. Static files was not loading on deployed site. In tasty_tales project, `settings.py` file Needed to move `cloudingry_storage` to below the `django.contrib.staticfiles`
<figure align="center">
    <img src="https://res.cloudinary.com/dcjkzptkn/image/upload/v1693244698/Testing/bugs/whitenoise-error-fix_xqcbsm.jpg"
        alt="WhiteNoise">
    <figcaption>WhiteNoise error</figcaption>
    </figure>
