document.addEventListener('DOMContentLoaded', function() {
    
    const openMenu = document.querySelector(".open-menu");
    const closeMenu = document.querySelector(".close-menu");
    const menuWrapper = document.querySelector(".menu-wrapper");
    const hasCollapsible = document.querySelectorAll(".has-collapsible");
    
    openMenu.addEventListener("click", function () {
        menuWrapper.classList.add("offcanvas");
    });
    closeMenu.addEventListener("click", function () {
        menuWrapper.classList.remove("offcanvas");
    });
   
    hasCollapsible.forEach(function (collapsible) {
        collapsible.addEventListener("click", function () {
            collapsible.classList.toggle("active");
           
            hasCollapsible.forEach(function (otherCollapsible) {
                if (otherCollapsible !== collapsible) {
                    otherCollapsible.classList.remove("active");
                }
            });
        });
    });
    });

    document.addEventListener('DOMContentLoaded', function() {
        function showLoader() {
            $("#loading").show();
        }
        function hideLoader() {
            $("#loading").hide();
        }

        $(".menu-child-item a").click(function(e) {
            showLoader();   
            e.preventDefault(); 
            var linkText = $(this).text();
            if (linkText == '1237 – 1241 Нашествие монголо-татарских войск во главе с ханом Батыем на Русь. Рост военных действий на территории русских княжеств.') {
                linkText = '1237 – 1241  монголо-татарских  во главе с ханом Батыем на Русь.';
            }
    
            const xhr = new XMLHttpRequest();
            xhr.open('POST', '/asd');
            
            xhr.setRequestHeader('Content-Type', 'application/json');
            
            xhr.onload = () => {
                if (xhr.status >= 200 && xhr.status < 300) {
                    window.location.href = '/asd';
                    hideLoader();
                } else {
                    console.error('Failed to make POST request to /asd');
                }
            };
            
            xhr.send(JSON.stringify({ linkText: linkText }));
            
        });
    })    
    document.addEventListener('DOMContentLoaded', function() {
        var image = document.getElementById('sec-image');
        image.addEventListener('click', function() {
        var imageUrl = image.src;
        window.location.href = imageUrl;
        });
})