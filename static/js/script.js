/** THEME MANAGEMENT ---------------------------------------------------------------- */


const docTheme = document.documentElement.className;
checkTheme(docTheme);



function setTheme(theme) {
    document.documentElement.className = theme;
    checkTheme(theme);
}

function checkTheme(theme) {
    if (theme == 'light') {  
        document.getElementById("navbar-themes").style.color = "var(--yellow-500)";
        document.getElementById("light_theme").style.color = "var(--yellow-500)";
        document.getElementById("dark_theme").style.color = "var(--text-color)";
        document.getElementById("deep_dark_theme").style.color = "var(--text-color)";
    } else if (theme == 'dark') {  
        document.getElementById("dark_theme").style.color = "var(--light-blue-500)";
        document.getElementById("navbar-themes").style.color = "var(--light-blue-500)";
        document.getElementById("light_theme").style.color = "var(--text-color)";
        document.getElementById("deep_dark_theme").style.color = "var(--text-color)";
    } else {
        document.getElementById("deep_dark_theme").style.color = "var(--primary-color)";
        document.getElementById("navbar-themes").style.color = "var(--primary-color)";
        document.getElementById("light_theme").style.color = "var(--text-color)";
        document.getElementById("dark_theme").style.color = "var(--text-color)";

    }
    
}
/** END THEME MANAGEMENT ---------------------------------------------------------------- */


/** NAVIGATION BARS ---------------------- -----------------------------*/
const navbar = document.getElementById("navbar");
const sidebar = document.getElementById("sidebar");
/** Explore LINKS in BARS ---------------------- -----------------------------*/
const navbar_exploreLink = document.getElementById("navbar-explore");
const sidebar_exploreLink = document.getElementById("sidebar-explore");
/** Categories LINKS in BARS ---------------------- -----------------------------*/
const navbar_categoriesLink = document.getElementById("navbar-categories");
const sidebar_categoriesLink = document.getElementById("sidebar-categories");
/** SUBMENUS TOGGLES */
const sidebarMenu = document.getElementById("navbar-more");
const mobileMenu = document.getElementById("mobile-menu");

function navbar_links_toggle(verifier) {
    document.getElementById("sidebar-" + verifier).style.color = "var(--primary-color-hover)";
    document.getElementById("navbar-" + verifier).style.color = "var(--primary-color-hover)";
    document.getElementById("navbar-" + verifier).classList.add("navbar-link-active");
    if (verifier != 'explore') {
        sidebar_exploreLink.style.color = "var(--text-color-inverse)";
        navbar_exploreLink.style.color = "var(--text-color)";
        navbar_exploreLink.classList.remove("navbar-link-active");
    } else if (verifier != 'categories') {
        sidebar_categoriesLink.style.color = "var(--text-color-inverse)";
        navbar_categoriesLink.style.color = "var(--text-color)";
        navbar_categoriesLink.classList.remove("navbar-link-active");
    } 
}

function lang_toggle(verifier) {
    if (verifier == '1') {
        document.getElementById("sidebar").style.display = "block";
        document.getElementById('navbar-more').setAttribute("onclick", "lang_toggle('0');");
    } else {
        document.getElementById("sidebar").style.display = "none";
        document.getElementById('navbar-more').setAttribute("onclick", "lang_toggle('1');")
    }
}

function navbar_theme_toggle(verifier) {
    if (verifier == '1') {
        document.getElementById("navbar-list-themes").style.display = "block";
        document.getElementById('navbar-themes').setAttribute("onclick", "navbar_theme_toggle('0');");
    } else {
        document.getElementById("navbar-list-themes").style.display = "none";
        document.getElementById('navbar-themes').setAttribute("onclick", "navbar_theme_toggle('1');")
    }
}

/*** -------------------------- */

const firstBanner = document.querySelector('#banner-content .banner-card:nth-child(1)');
const secondBanner = document.querySelector('#banner-content .banner-card:nth-child(2)');
const thirdBanner = document.querySelector('#banner-content .banner-card:nth-child(3)');

function firstBanner_active() {
    firstBanner.style.display = 'block';
    secondBanner.style.display = 'none';
    thirdBanner.style.display = 'none';
}
function secondBanner_active() {
    firstBanner.style.display = 'none';
    secondBanner.style.display = 'block';
    thirdBanner.style.display = 'none';
}
function thirdBanner_active() {
    firstBanner.style.display = 'none';
    secondBanner.style.display = 'none';
    thirdBanner.style.display = 'block';
}

function allBanner_active(){
    firstBanner.style.display = 'block';
    secondBanner.style.display = 'block';
    thirdBanner.style.display = 'block';
}
mobile();
function mobile(){

    const mql = window.matchMedia('screen and (max-width: 575px)');

    checkMedia(mql);
    mql.addListener(checkMedia);

    function checkMedia(mql){

        if(mql.matches){
            mobileMenu.style.display = "block";
            console.log('Mobile');


            firstBanner_active();
            changeBanner();
            function changeBanner() {
                firstBanner_active();
                setTimeout(function () {
                    secondBanner_active();
                    setTimeout(function () {
                        thirdBanner_active();
                        setTimeout(function () {
                            changeBanner();        
                        }, 3500);
    
                    }, 3500);

                }, 3500);
            }

        }
    }
}

tablet();

function tablet(){

    const mql = window.matchMedia('screen and (min-width: 576px) and (max-width: 1024px)');

    checkMedia(mql);
    mql.addListener(checkMedia);

    function checkMedia(mql){

        if(mql.matches){

            allBanner_active();
            console.log('tablet');
            sidebar.style.display = "none";

        }
    }
}
desktop();

function desktop(){

    const mql = window.matchMedia('screen and (min-width: 1025px) and (max-width: 1920px)');

    checkMedia(mql);
    mql.addListener(checkMedia);

    function checkMedia(mql){

        if (mql.matches) {
            allBanner_active();
            
            mobileMenu.style.display = "none";

            console.log('desktop');
        }
    }
}