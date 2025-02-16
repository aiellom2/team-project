// sidebar-menu.js

// Function to load the sidebar based on user type
// Function to load the sidebar based on user type
function loadSidebar() {
    const sidebarContainer = document.querySelector('#sidebar-wrapper');
    if (sidebarContainer) {
        // Determine user type from URL
        const path = window.location.pathname;
        let baseUrl;
                
        if (path.includes('/teacher')) {
            baseUrl = '/teacher';
        
            sidebarContainer.innerHTML = `
            <div class="sidebar-heading border-bottom bg-light">Project Reviews</div>
            <div class="list-group list-group-flush">
                <a class="list-group-item list-group-item-action list-group-item-light p-3" href="${baseUrl}-main">Main</a>
                <a class="list-group-item list-group-item-action list-group-item-light p-3" href="${baseUrl}-students">Students</a>
                <a class="list-group-item list-group-item-action list-group-item-light p-3" href="${baseUrl}-objectives">Objectives</a>
                <a class="list-group-item list-group-item-action list-group-item-light p-3" href="${baseUrl}-users">Users</a>
                <a class="list-group-item list-group-item-action list-group-item-light p-3" href="${baseUrl}-needs">Needs</a>
                <a class="list-group-item list-group-item-action list-group-item-light p-3" href="${baseUrl}-stories">Stories</a>
                <a class="list-group-item list-group-item-action list-group-item-light p-3" href="${baseUrl}-features">Features</a>
                <a class="list-group-item list-group-item-action list-group-item-light p-3" href="${baseUrl}-diagrams">Diagrams</a>
                <a class="list-group-item list-group-item-action list-group-item-light p-3" href="${baseUrl}-reports">Reports</a>
        
            </div>
        `;
        
        } else if (path.includes('/admin')) {
            baseUrl = '/admin';
        
            sidebarContainer.innerHTML = `
            <div class="sidebar-heading border-bottom bg-light">Report Reviews</div>
            <div class="list-group list-group-flush">
                <a class="list-group-item list-group-item-action list-group-item-light p-3" href="${baseUrl}-main">Main</a>      
                <a class="list-group-item list-group-item-action list-group-item-light p-3" href="${baseUrl}-teachers">Teachers</a>
                <a class="list-group-item list-group-item-action list-group-item-light p-3" href="${baseUrl}-students">Students</a>
                <a class="list-group-item list-group-item-action list-group-item-light p-3" href="${baseUrl}-reports">Reports</a>
               
            </div>
        `;
        
        } else {
        
        
            baseUrl = '/student';
        
        sidebarContainer.innerHTML = `
            <div class="sidebar-heading border-bottom bg-light">Project Proposals</div>
            <div class="list-group list-group-flush">
                <a class="list-group-item list-group-item-action list-group-item-light p-3" href="${baseUrl}-main">Main</a>      
                <a class="list-group-item list-group-item-action list-group-item-light p-3" href="${baseUrl}-objectives">Objectives</a>
                <a class="list-group-item list-group-item-action list-group-item-light p-3" href="${baseUrl}-users">Users</a>
                <a class="list-group-item list-group-item-action list-group-item-light p-3" href="${baseUrl}-needs">Needs</a>
                <a class="list-group-item list-group-item-action list-group-item-light p-3" href="${baseUrl}-stories">Stories</a>
                <a class="list-group-item list-group-item-action list-group-item-light p-3" href="${baseUrl}-features">Features</a>
                <a class="list-group-item list-group-item-action list-group-item-light p-3" href="${baseUrl}-diagrams">Diagrams</a>
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
