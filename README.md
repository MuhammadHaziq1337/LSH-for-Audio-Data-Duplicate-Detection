# Locality Sensitive Hashing (LSH) for Audio Data Duplicate Detection

## Objective

Implement Locality Sensitive Hashing (LSH) on audio data to detect duplicates and explore additional interesting findings from LSH on audio data. Develop a responsive Flask application for audio similarity search.

## Tasks

### Part-I

#### Q1:

1. **Pre-Processing of Audio Files:**
   - Extract the Mel-Frequency Cepstral Coefficients (MFCCs) from the audio files.

2. **Create LSH Hash Tables:**
   - Determine the appropriate number of tables and hash size.
   - Create feature vectors (MFCC) and run a query on the LSH tables for a new audio file.
   - Compare the feature vector of the new audio with the matches returned by LSH using a chosen metric (L2 distance, cosine similarity, or Jaccard similarity).
   - Return the best match based on the metric.

#### Q2:

- Explore additional interesting findings from LSH on audio data beyond duplicate detection.

### Part-II

Develop a responsive Flask application with the following functionalities:

- Upload Audio file (MP4).
- Show audio similarity results if any.
- Implement the findings from Q2.

## Implementation

### Preprocessing Steps

1. **Extract MFCCs:**
   - Use the `librosa` library to extract MFCC features from the audio files.

2. **Create LSH Hash Tables:**
   - Use MinHash and LSH algorithms to create hash tables.
   - Store the minhashes for each audio file.

3. **Feature Vector and Query:**
   - Generate a feature vector (MFCC) for a new audio file.
   - Query the LSH tables to find similar audio files.
   - Compare using a chosen similarity metric and return the best match.

### Interesting Findings from LSH (Q2)

- Beyond duplicate detection, LSH can be used for:
  - Audio classification.
  - Identifying audio genres.
  - Clustering similar audio files.

## Flask Application

### Routes

1. **'/' Route:**
   - Renders an HTML page allowing users to upload an audio file.

2. **'/upload' Route:**
   - Handles file upload and similarity search.
   - Calculates minhash for the uploaded audio file.
   - Uses LSH to find similar audio files.
   - Displays similarity results.

### Tools and Libraries

- **Python:**
  - `librosa` for audio processing.
  - `numpy` and `pandas` for data handling.
  - `sklearn` for MinHash and LSH implementation.
  - `pickle` for saving and loading minhashes.
- **Flask:**
  - For building the web application.
- **HTML/CSS:**
  - For creating the user interface.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/audio-lsh.git
