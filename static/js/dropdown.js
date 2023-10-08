
    document.addEventListener('DOMContentLoaded', function() {
        const dropdownButton = document.querySelector('.dropdown-button');
        const dropdownContent = document.querySelector('.dropdown-content');

        dropdownButton.addEventListener('click', function() {
            dropdownContent.style.display = dropdownContent.style.display === 'block' ? 'none' : 'block';
        });

        const options = dropdownContent.querySelectorAll('a');
        const location = dropdownButton.getAttribute('name');
        console.log(location);
        options.forEach(function(option) {
            option.addEventListener('click', function(event) {
                const optionName = option.getAttribute('name');
                fetch('/filterByMeal', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ option: optionName, location: location}),
                })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
            })
        });

        
    
        //     option.addEventListener('click', function(event) {
        //         event.preventDefault(); // Prevent the default link behavior
    
        //         const optionName = option.getAttribute('name');
        //         console.log(optionName);
        //         const location = dropdownContent.getAttribute('name');
        //         // Send the option name to the Flask server using a POST request
        //         fetch('/filterByMeal', {
        //             method: 'POST',
        //             headers: {
        //                 'Content-Type': 'application/jso',
        //             },
        //             body: JSON.stringify({ option: optionName, location: location}),
        //         })
        //         .then(response => {
        //             if (!response.ok) {
        //                 throw new Error('Network response was not ok');
        //             }
        //             return response.json();
        //         })
        //         .then(data => {
        //             // Handle the response from the server as needed
        //             console.log('Response from Flask:', data);
        //         })
        //         .catch(error => {
        //             console.error('Error:', error);
        //         });
        //     });
        // });
    });

