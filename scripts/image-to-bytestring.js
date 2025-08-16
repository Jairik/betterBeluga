/** Helper js function to convert an image to a bytestring, given it's path */
const fs = require('fs');

/** Converts an image file to a bytestring.
 * @param {string} imagePath The path to the image file
 * @returns {string} The bytestring representation
 */
function imageToBytestring(imagePath) {
    try {
        const imageBuffer = fs.readFileSync(imagePath);
        return imageBuffer.toString('base64');
    } catch (error) {
        console.error('Error reading the image file:', error);
        throw error;
    }
}

module.exports = imageToBytestring;