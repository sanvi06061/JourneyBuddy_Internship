\# Redis In-Memory Data Store – Cache-Aside Pattern



\## Overview



This project demonstrates a Redis caching strategy using FastAPI and the Cache-Aside Pattern.



The application simulates a user profile database and uses Redis as a fast in-memory cache for frequently accessed user profiles.



\## Objectives



\- Implement Redis as an in-memory cache.

\- Demonstrate the Cache-Aside Pattern.

\- Handle cache hits and cache misses.

\- Retrieve data from persistent storage on cache misses.

\- Store retrieved data in Redis.

\- Apply a strict 60-second TTL.

\- Demonstrate automatic cache expiration.

\- Implement cache invalidation.



\## Architecture



```text

Client

&#x20;  |

&#x20;  v

FastAPI Application

&#x20;  |

&#x20;  v

Check Redis Cache

&#x20;  |

&#x20;  +---- Cache HIT ------> Return cached profile

&#x20;  |

&#x20;  +---- Cache MISS -----> Read from Database

&#x20;                             |

&#x20;                             v

&#x20;                        Store in Redis

&#x20;                          TTL = 60s

&#x20;                             |

&#x20;                             v

&#x20;                        Return profile

