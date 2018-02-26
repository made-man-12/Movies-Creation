import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">

  <head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="Movie Website Creation">
    <meta name="author" content="mademan12">

    <title>My Movie List</title>

    <!-- Bootstrap core CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">


    <!-- Custom fonts for this template -->
    <link href="https://fonts.googleapis.com/css?family=Montserrat:400,700" rel="stylesheet" type="text/css">
    <link href="https://fonts.googleapis.com/css?family=Lato:400,700,400italic,700italic" rel="stylesheet" type="text/css">

    <!-- Plugin CSS -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/magnific-popup.js/1.1.0/magnific-popup.css" rel="stylesheet" type="text/css">

    <!-- Custom styles for this template -->
    <link href="freelancer.min.css" rel="stylesheet">

  </head>
'''


# The main page layout and title bar
main_page_content = '''
  <body id="page-top">

    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg bg-secondary fixed-top text-uppercase" id="mainNav">
      <div class="container">
        <a class="navbar-brand js-scroll-trigger" href="#page-top">Movie Website</a>
        <button class="navbar-toggler navbar-toggler-right text-uppercase bg-primary text-white rounded" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
          Menu
          <i class="fa fa-bars"></i>
        </button>
        <div class="collapse navbar-collapse" id="navbarResponsive">
          <ul class="navbar-nav ml-auto">
            <li class="nav-item mx-0 mx-lg-1">
              <a class="nav-link py-3 px-0 px-lg-3 rounded js-scroll-trigger" href="#movie">Movie</a>
            </li>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <!-- Header -->
    {site_header}
    <!-- Movies Grid Section -->
    <section class="portfolio" id="movie">
      <div class="container">
        <h2 class="text-center text-uppercase text-secondary mb-0">Portfolio</h2>
        <hr class="star-dark mb-5">
        <div class="row">
          {site_content}
        </div>
      </div>
    </section>
    <!-- Footer -->
    <div class="copyright py-4 text-center text-white">
      <div class="container">
        <small>Copyright &copy; One Million Arab Coders</small>
      </div>
    </div>

    <!-- Scroll to Top Button (Only visible on small and extra-small screen sizes) -->
    <div class="scroll-to-top d-lg-none position-fixed ">
      <a class="js-scroll-trigger d-block text-center text-white rounded" href="#page-top">
        <i class="fa fa-chevron-up"></i>
      </a>
    </div>
    <!-- Portfolio Modals -->
     {info_box}
     
     <!-- Bootstrap core JavaScript -->
        <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    
        <!-- Plugin JavaScript -->
        <script src="https://cdnjs.cloudflare.com/ajax/libs/magnific-popup.js/1.1.0/jquery.magnific-popup.min.js"></script>
    
    
        <!-- Custom scripts for this template -->
        <script src="freelancer.min.js"></script>
        <script src="https://use.fontawesome.com/5468e16057.js"></script>
  </body>
</html>
'''
#Header
movie_header = '''
<header class="masthead bg-primary text-white text-center" style="
    background-image: url('{header_img}');">
  <div class="container">
    <div class= "cool">
        <h1 class="text-uppercase mb-0">{header_title}</h1>
        <hr class="star-light">
        <h2 class="font-weight-light mb-0">{header_desc}</h2>
    </div>
  </div>
</header>

'''

# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4">
    <a class="portfolio-item d-block mx-auto" href="#portfolio-modal-{movie_id}">
      <div class="portfolio-item-caption d-flex position-absolute h-100 w-100">
        <div class="portfolio-item-caption-content my-auto w-100 text-center text-white">
          <i class="fa fa-search-plus fa-3x"></i>
        </div>
      </div>
      <img class="img-fluid" src="{poster_image_url}" alt="">
    </a>
</div>
'''
#Info box
movie_info_content ='''
<div class="portfolio-modal mfp-hide" id="portfolio-modal-{movie_id}">
  <div class="portfolio-modal-dialog bg-white">
    <a class="close-button d-none d-md-block portfolio-modal-dismiss" href="#">
      <i class="fa fa-3x fa-times"></i>
    </a>
    <div class="container text-center">
      <div class="row">
        <div class="col-lg-8 mx-auto">
          <h2 class="text-secondary text-uppercase mb-0">{movie_title}</h2>
          <hr class="star-dark mb-5">
          <iframe width="854" height="480" src="https://www.youtube.com/embed/{trailer_youtube_id}?ecver=1" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen="" style="max-width: 100%;"></iframe>
          <p class="mb-5">{movie_storyline}</p>
          <a class="btn btn-primary btn-lg rounded-pill portfolio-modal-dismiss" href="#">
            <i class="fa fa-close"></i>
            Close Movie</a>
        </div>
      </div>
    </div>
  </div>
</div>
'''

# A Style
css = '''
body{font-family:Lato}h1,h2,h3,h4,h5,h6{font-weight:700;font-family:Montserrat}hr.star-dark,hr.star-light{max-width:15rem;padding:0;text-align:center;border:none;border-top:solid .25rem;margin-top:2.5rem;margin-bottom:2.5rem}hr.star-dark:after,hr.star-light:after{position:relative;top:-.8em;display:inline-block;padding:0 .25em;font-family:FontAwesome;font-size:2em}hr.star-light{border-color:#fff}hr.star-light:after{color:#fff;background-color:#18bc9c}hr.star-dark{border-color:#000}hr.star-dark:after{color:#000;background-color:#fff}section{padding:6rem 0}section h2{font-size:2.25rem;line-height:2rem}@media (min-width:992px){section h2{font-size:3rem;line-height:2.5rem}}.btn-xl{padding:1rem 1.75rem;font-size:1.25rem}.btn-social{width:3.25rem;height:3.25rem;font-size:1.25rem;line-height:2rem}.scroll-to-top{z-index:1042;right:1rem;bottom:1rem;display:none}.scroll-to-top a{width:3.5rem;height:3.5rem;background-color:rgba(33,37,41,.5);line-height:3.1rem}#mainNav{padding-top:1rem;padding-bottom:1rem;font-weight:700;font-family:Montserrat}#mainNav .navbar-brand{color:#fff}#mainNav .navbar-nav{margin-top:1rem;letter-spacing:.0625rem}#mainNav .navbar-nav li.nav-item a.nav-link{color:#fff}#mainNav .navbar-nav li.nav-item a.nav-link:hover{color:#18bc9c}#mainNav .navbar-nav li.nav-item a.nav-link:active,#mainNav .navbar-nav li.nav-item a.nav-link:focus{color:#fff}#mainNav .navbar-nav li.nav-item a.nav-link.active{color:#18bc9c}#mainNav .navbar-toggler{font-size:80%;padding:.8rem}@media (min-width:992px){#mainNav{padding-top:1.5rem;padding-bottom:1.5rem;-webkit-transition:padding-top .3s,padding-bottom .3s;-moz-transition:padding-top .3s,padding-bottom .3s;transition:padding-top .3s,padding-bottom .3s}#mainNav .navbar-brand{font-size:2em;-webkit-transition:font-size .3s;-moz-transition:font-size .3s;transition:font-size .3s}#mainNav .navbar-nav{margin-top:0}#mainNav .navbar-nav>li.nav-item>a.nav-link.active{color:#fff;background:#18bc9c}#mainNav .navbar-nav>li.nav-item>a.nav-link.active:active,#mainNav .navbar-nav>li.nav-item>a.nav-link.active:focus,#mainNav .navbar-nav>li.nav-item>a.nav-link.active:hover{color:#fff;background:#18bc9c}#mainNav.navbar-shrink{padding-top:.5rem;padding-bottom:.5rem}#mainNav.navbar-shrink .navbar-brand{font-size:1.5em}}header.masthead{padding-top:calc(6rem + 72px);padding-bottom:6rem}header.masthead h1{font-size:3rem;line-height:3rem}header.masthead h2{font-size:1.3rem;font-family:Lato}@media (min-width:992px){header.masthead{padding-top:calc(6rem + 106px);padding-bottom:6rem}header.masthead h1{font-size:4.75em;line-height:4rem}header.masthead h2{font-size:1.75em}}.portfolio{margin-bottom:-15px}.portfolio .portfolio-item{position:relative;display:block;max-width:25rem;margin-bottom:15px}.portfolio .portfolio-item .portfolio-item-caption{-webkit-transition:all ease .5s;-moz-transition:all ease .5s;transition:all ease .5s;opacity:0;background-color:rgba(24,188,156,.9)}.portfolio .portfolio-item .portfolio-item-caption:hover{opacity:1}.portfolio .portfolio-item .portfolio-item-caption .portfolio-item-caption-content{font-size:1.5rem}@media (min-width:576px){.portfolio{margin-bottom:-30px}.portfolio .portfolio-item{margin-bottom:30px}}.portfolio-modal .portfolio-modal-dialog{padding:3rem 1rem;min-height:calc(100vh - 2rem);margin:1rem calc(1rem - 8px);position:relative;z-index:2;-moz-box-shadow:0 0 3rem 1rem rgba(0,0,0,.5);-webkit-box-shadow:0 0 3rem 1rem rgba(0,0,0,.5);box-shadow:0 0 3rem 1rem rgba(0,0,0,.5)}.portfolio-modal .portfolio-modal-dialog .close-button{position:absolute;top:2rem;right:2rem}.portfolio-modal .portfolio-modal-dialog .close-button i{line-height:38px}.portfolio-modal .portfolio-modal-dialog h2{font-size:2rem}@media (min-width:768px){.portfolio-modal .portfolio-modal-dialog{min-height:100vh;padding:5rem;margin:3rem calc(3rem - 8px)}.portfolio-modal .portfolio-modal-dialog h2{font-size:3rem}}.floating-label-form-group{position:relative;border-bottom:1px solid #e9ecef}.floating-label-form-group input,.floating-label-form-group textarea{font-size:1.5em;position:relative;z-index:1;padding-right:0;padding-left:0;resize:none;border:none;border-radius:0;background:0 0;box-shadow:none!important}.floating-label-form-group label{font-size:.85em;line-height:1.764705882em;position:relative;z-index:0;top:2em;display:block;margin:0;-webkit-transition:top .3s ease,opacity .3s ease;-moz-transition:top .3s ease,opacity .3s ease;-ms-transition:top .3s ease,opacity .3s ease;transition:top .3s ease,opacity .3s ease;vertical-align:middle;vertical-align:baseline;opacity:0}.floating-label-form-group:not(:first-child){padding-left:14px;border-left:1px solid #e9ecef}.floating-label-form-group-with-value label{top:0;opacity:1}.floating-label-form-group-with-focus label{color:#18bc9c}form .row:first-child .floating-label-form-group{border-top:1px solid #e9ecef}.footer{padding-top:5rem;padding-bottom:5rem;background-color:#000;color:#fff}.copyright{background-color:#1a252f}a{color:#18bc9c}a:active,a:focus,a:hover{color:#128f76}.btn{border-width:2px}.bg-primary{background-color:#18bc9c!important}.bg-secondary{background-color:#000!important}.text-primary{color:#18bc9c!important}.text-secondary{color:#000!important}.btn-primary{background-color:#18bc9c;border-color:#18bc9c}.btn-primary:active,.btn-primary:focus,.btn-primary:hover{background-color:#128f76;border-color:#128f76}.btn-secondary{background-color:#000;border-color:#000}.btn-secondary:active,.btn-secondary:focus,.btn-secondary:hover{background-color:#1a252f;border-color:#1a252f}.cool{margin: 100px auto;}

'''

#JS
js = '''
!function(o){"use strict";o('a.js-scroll-trigger[href*="#"]:not([href="#"])').click(function(){if(location.pathname.replace(/^\//,"")==this.pathname.replace(/^\//,"")&&location.hostname==this.hostname){var t=o(this.hash);if((t=t.length?t:o("[name="+this.hash.slice(1)+"]")).length)return o("html, body").animate({scrollTop:t.offset().top-70},1e3,"easeInOutExpo"),!1}}),o(document).scroll(function(){o(this).scrollTop()>100?o(".scroll-to-top").fadeIn():o(".scroll-to-top").fadeOut()}),o(".js-scroll-trigger").click(function(){o(".navbar-collapse").collapse("hide")}),o("body").scrollspy({target:"#mainNav",offset:80});var t=function(){o("#mainNav").offset().top>100?o("#mainNav").addClass("navbar-shrink"):o("#mainNav").removeClass("navbar-shrink")};t(),o(window).scroll(t),o(".portfolio-item").magnificPopup({type:"inline",preloader:!1,focus:"#username",modal:!0}),o(document).on("click",".portfolio-modal-dismiss",function(t){t.preventDefault(),o.magnificPopup.close()}),o(function(){o("body").on("input propertychange",".floating-label-form-group",function(t){o(this).toggleClass("floating-label-form-group-with-value",!!o(t.target).val())}).on("focus",".floating-label-form-group",function(){o(this).addClass("floating-label-form-group-with-focus")}).on("blur",".floating-label-form-group",function(){o(this).removeClass("floating-label-form-group-with-focus")})})}(jQuery);
'''

def create_movie_header(header):
    # The HTML content for this section of the page
    content = ''

    content += movie_header.format(
        header_title=header[0],
        header_desc=header[1],
        header_img=header[2]
    )
    return content

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    count = 0
    for movie in movies:
        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            poster_image_url=movie.poster_image_url,
            movie_id = count
        )
        count += 1
    return content

def create_movie_content_box(movies):
    # The HTML content for this section of the page
    content = ''
    count = 0
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
        else None)

        # Append the tile for the movie with its content filled in
        content += movie_info_content.format(
            movie_title = movie.title,
            movie_storyline = movie.storyline,
            poster_image_url = movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            movie_id=count
        )
        count += 1
    return content


def open_movies_page(movies, header):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        site_header = create_movie_header(header),
        site_content= create_movie_tiles_content(movies),
        info_box = create_movie_content_box(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # Create css file or overwrite
    css_file = open('freelancer.min.css', 'w')

    # Output the css file
    css_file.write(css)
    css_file.close()

    # Create js file or overwrite
    js_file = open('freelancer.min.js', 'w')

    # Output the js file
    js_file.write(js)
    js_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
