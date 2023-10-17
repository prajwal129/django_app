document.addEventListener('DOMContentLoaded', function () {
    const reasonField = document.querySelector('#id_outpass_reason');
    const inTimeField = document.querySelector('#id_in_time');

    // Define in-time options for the "Business" reason
    const businessInTimeOptions = [
        ['08:00', '8:00 AM'],
        ['09:00', '9:00 AM'],
        // Add more options as needed
    ];

    // Function to update in-time options based on the selected reason
    function updateInTimeOptions() {
        const selectedReason = reasonField.value;
        inTimeField.innerHTML = '';

        if (selectedReason === 'business') {
            businessInTimeOptions.forEach(([value, label]) => {
                const option = document.createElement('option');
                option.value = value;
                option.text = label;
                inTimeField.appendChild(option);
            });
        }
    }

    // Initial update of in-time options
    updateInTimeOptions();

    // Listen for changes in the reason field
    reasonField.addEventListener('change', updateInTimeOptions);
});
