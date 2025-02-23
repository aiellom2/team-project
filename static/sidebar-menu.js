// sidebar-menu.js

// Function to load the sidebar based on user type
// Function to load the sidebar based on user type
function loadSidebar() {
    const sidebarContainer = document.querySelector('#sidebar-wrapper');
    if (sidebarContainer) {
        // Determine user type from URL
        const path = window.location.pathname;
        let baseUrl;
                
        if (path.includes('/manager')) {
            baseUrl = '/manager';
        
            sidebarContainer.innerHTML = `
            <div class="sidebar-heading border-bottom bg-light">Project Reviews</div>
            <div class="list-group list-group-flush">
                <a class="list-group-item list-group-item-action list-group-item-light p-3" href="${baseUrl}-main">Main</a>
                <a class="list-group-item list-group-item-action list-group-item-light p-3" href="${baseUrl}-employees">Employees</a>
                <a class="list-group-item list-group-item-action list-group-item-light p-3" href="${baseUrl}-vacation-requests">Vacation Requests</a>
                <a class="list-group-item list-group-item-action list-group-item-light p-3" href="${baseUrl}-supplies-requests">Supplies Requests</a>

                
        
            </div>
        `;
        
        } else if (path.includes('/admin')) {
            baseUrl = '/admin';
        
            sidebarContainer.innerHTML = `
            <div class="sidebar-heading border-bottom bg-light">Report Reviews</div>
            <div class="list-group list-group-flush">
                <a class="list-group-item list-group-item-action list-group-item-light p-3" href="${baseUrl}-main">Main</a>
                <a class="list-group-item list-group-item-action list-group-item-light p-3" href="${baseUrl}-employees">Employees</a>      
                <a class="list-group-item list-group-item-action list-group-item-light p-3" href="${baseUrl}-managers">Managers</a>
                <a class="list-group-item list-group-item-action list-group-item-light p-3" href="${baseUrl}-requests">Requests</a>      
                <a class="list-group-item list-group-item-action list-group-item-light p-3" href="${baseUrl}-reports">Reports</a>      

               
            </div>
        `;
        
        } else {
        
        
            baseUrl = '/employee';
        
        sidebarContainer.innerHTML = `
            <div class="sidebar-heading border-bottom bg-light">Project Proposals</div>
            <div class="list-group list-group-flush">
                <a class="list-group-item list-group-item-action list-group-item-light p-3" href="${baseUrl}-main">Main</a>      
                <a class="list-group-item list-group-item-action list-group-item-light p-3" href="${baseUrl}-vacation-requests">Vacation Requests</a>      
                <a class="list-group-item list-group-item-action list-group-item-light p-3" href="${baseUrl}-supplies-requests">Supplies Requests</a>      

            </div>
        `;
        
        }
                
    }
}

// Function to handle sidebar toggle
function enableSidebarToggle() {
    const sidebarToggle = document.body.querySelector('#sidebarToggle');
    if (sidebarToggle) {
        // Uncomment to persist sidebar toggle state
        // if (localStorage.getItem('sb|sidebar-toggle') === 'true') {
        //     document.body.classList.toggle('sb-sidenav-toggled');
        // }

        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        });
    }
}

// Call both functions after page load
window.addEventListener('DOMContentLoaded', () => {
    loadSidebar();
    enableSidebarToggle();
});
