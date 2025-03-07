
function loadSidebar() {
    const sidebarContainer = document.querySelector('#sidebar-wrapper');
    if (sidebarContainer) {

        const path = window.location.pathname;
        let baseUrl;
                
        if (path.includes('/admin')) {
            baseUrl = '/admin';
        
            sidebarContainer.innerHTML = `
            <div class="sidebar-heading border-bottom bg-light">Admin</div>
            <div class="list-group list-group-flush">
                <a class="list-group-item list-group-item-action list-group-item-light p-3" href="${baseUrl}-main">Main</a>
                <a class="list-group-item list-group-item-action list-group-item-light p-3" href="${baseUrl}-request-types">Request Types</a>
                <a class="list-group-item list-group-item-action list-group-item-light p-3" href="${baseUrl}-managers">Managers</a>
                <a class="list-group-item list-group-item-action list-group-item-light p-3" href="${baseUrl}-employees">Employees</a>
                <a class="list-group-item list-group-item-action list-group-item-light p-3" href="${baseUrl}-office-supplies">Office Supplies</a>

        
            </div>
        `;
        
        } else if (path.includes('/manager')) {
            baseUrl = '/manager';
        
            sidebarContainer.innerHTML = `
            <div class="sidebar-heading border-bottom bg-light">Manager</div>
            <div class="list-group list-group-flush">
                <a class="list-group-item list-group-item-action list-group-item-light p-3" href="${baseUrl}-main">Main</a>
                  
            </div>
        `;
        
        } else {
        
        
            baseUrl = '/employee';
        
        sidebarContainer.innerHTML = `
            <div class="sidebar-heading border-bottom bg-light">Employee</div>
            <div class="list-group list-group-flush">
                <a class="list-group-item list-group-item-action list-group-item-light p-3" href="${baseUrl}-main">Main</a>      
                

            </div>
        `;
        
        }
                
    }
}

function enableSidebarToggle() {
    const sidebarToggle = document.body.querySelector('#sidebarToggle');
    if (sidebarToggle) {

        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        });
    }
}

window.addEventListener('DOMContentLoaded', () => {
    loadSidebar();
    enableSidebarToggle();
});
