import concurrent.futures
import logging
import time

logging.basicConfig( filename="logs.txt",level=logging.INFO, format='%(asctime)s - %(message)s')

def integrate(f, a, b, *, n_jobs=1, n_iter=10000000):
    
    start_time = time.time()
    
    step = (b - a) / n_iter
    chunk_size = n_iter // n_jobs

    def integrate_chunk(chunk_start):
        chunk_acc = 0
        chunk_end = chunk_start + chunk_size
        for i in range(chunk_start, chunk_end):
            chunk_acc += f(a + i * step) * step
        return chunk_acc

    acc = 0

    with concurrent.futures.ProcessPoolExecutor(max_workers=n_jobs) as executor:
        future_to_chunk = {executor.submit(integrate_chunk, chunk_start): chunk_start for chunk_start in range(0, n_iter, chunk_size)}
        for future in concurrent.futures.as_completed(future_to_chunk):
            chunk_start = future_to_chunk[future]
            try:
                chunk_result = future.result()
            except Exception as exc:
                logging.error(f"Chunk {chunk_start} - {chunk_start + chunk_size}: {exc}")
            else:
                acc += chunk_result
                logging.info(f"Chunk {chunk_start} - {chunk_start + chunk_size} completed")
    end_time = time.time()
    logging.info(f"Time: {end_time-start_time}")
    return acc, end_time-start_time



