document.addEventListener('DOMContentLoaded', function() {
    const view360Modal = document.getElementById('view360Modal');
    let panorama, viewer; // Keep references to dispose of them later

    view360Modal.addEventListener('show.bs.modal', function(event) {
        // Button that triggered the modal
        const button = event.relatedTarget;
        // Get the image path from the data-panorama attribute
        const panoramaImage = button.getAttribute('data-panorama');

        const container = document.getElementById('panorama-container');

        // Create a new panorama and viewer
        panorama = new PANOLENS.ImagePanorama(panoramaImage);
        viewer = new PANOLENS.Viewer({ container: container });
        viewer.add(panorama);
    });

    // Important: Destroy the viewer when the modal is hidden to free up memory
    view360Modal.addEventListener('hide.bs.modal', function() {
        if (viewer) {
            viewer.destroy();
        }
    });
});
// Check if the map element exists on the current page
if (document.getElementById('map')) {
    // Initialize the map and set its view to Sikkim's coordinates
    const map = L.map('map').setView([27.5330, 88.5122], 9);

    // Add a tile layer from OpenStreetMap
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    // --- AI Integration Concept ---
    // This function would fetch data from your AI backend
    async function getAiRecommendations(userPreferences) {
        // In a real app, you would make an API call:
        // const response = await fetch('https://yourapi.com/get-sikkim-route', {
        //   method: 'POST',
        //   body: JSON.stringify(userPreferences)
        // });
        // const data = await response.json();
        // return data;

        // For demonstration, we use mock data:
        console.log("Fetching AI-powered recommendations...");
        return [
            { name: "Tsomgo Lake", type: "Nature", coords: [27.3736, 88.7618], info: "A stunning glacial lake." },
            { name: "Rumtek Monastery", type: "Culture", coords: [27.2845, 88.5681], info: "A vibrant hub of Tibetan Buddhism." }
        ];
    }

    // Add markers to the map based on AI recommendations
    getAiRecommendations({ interest: "nature" }).then(locations => {
        locations.forEach(loc => {
            L.marker(loc.coords)
              .addTo(map)
              .bindPopup(`<b>${loc.name}</b><br>${loc.info}`);
        });
    });
}
// Add this to your existing script.js file

document.addEventListener('DOMContentLoaded', function() {
    
    // Check if the registration form exists on the current page
    const registrationForm = document.getElementById('registration-form');

    if (registrationForm) {
        const password = document.getElementById('password');
        const confirmPassword = document.getElementById('confirmPassword');
        const errorDiv = document.getElementById('password-match-error');

        registrationForm.addEventListener('submit', function(event) {
            // Prevent form submission
            event.preventDefault();

            if (password.value !== confirmPassword.value) {
                // Show error message and add invalid class
                confirmPassword.classList.add('is-invalid');
                errorDiv.style.display = 'block';
            } else {
                // Passwords match, remove error and submit
                confirmPassword.classList.remove('is-invalid');
                errorDiv.style.display = 'none';

                // In a real application, you would now send the form data to your backend server
                console.log('Form is valid and ready to be sent to the backend.');
                alert('Registration successful! (Frontend demo)');
                // registrationForm.submit(); // Uncomment this line to allow actual submission
            }
        });
    }

    // --- Keep your other JS code (modal, map, etc.) below ---
    
});