# Research
<style scoped>
.article-container {
  display: flex;
  justify-content: space-between;
  gap: 20px;
  margin: 20px;
}

.article {
  width: 48%;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  padding: 20px;
  border-radius: 8px;
  background-color: #fff;
}

.article-image {
  width: 100%;
  height: auto;
  border-radius: 8px;
}

.article-description {
  margin-top: 15px;
  font-size: 16px;
  line-height: 1.5;
  color: #333;
}
</style>

<img src="/public/apple-touch-icon.png" alt="My Photo" style="width: 100%; height: 100%;">
The overarching goal of the SAFARI Research Group is to design fundamentally better computer architectures that will have long-lasting positive impact on human lives. We aim to invent computer architecture paradigms that get widely used for decades to come. The group develops both theoretical and practical ideas, methods, and infrastructures to understand, model and enhance performance, energy efficiency, reliability, security, safety, predictability, dependability, usability, and scalability of computer architectures. We have an extensive research & education portfolio centered around computer architecture and systems, with significant concerted efforts in all aspects of memory & storage, hardware security/safety/reliability, and system design for bioinformatics, medicine, and machine learning (with special focus on genome analysis).

Memory (and data movement from memory) is a key bottleneck in all computing systems. We tackle key problems in computer memory systems, spanning circuits to algorithms/applications. We rigorously study how to make memory systems fundamentally secure/safe/reliable, low-latency, predictable, and energy efficient and how to customize them for emerging applications like genomics, artificial intelligence, medical/health systems. Solutions to memory technology scaling problems, data-centric computing paradigms (Processing-in-Memory), and algorithm-architecture co-design for fast & efficient genome analysis are three major directions.  Although we have broad research interests in computing, we are especially interested in holistic architectural solutions that involve intelligent and efficient cooperation between the algorithm designer, the programmer, the compiler, the instruction set architecture, the microarchitecture, and the underlying circuits.The group has strong collaborations with industry and an extensive open-source teaching portfolio at BS/MS/PhD levels.
***
A sampling of our research areas includes:

**A. New Memory & Storage Architectures**

DRAM (Dynamic Random Access Memory) is the predominant technology used for computer memory. It is facing significant challenges in technology scaling, reliability, data retention, latency, bandwidth and power consumption. These greatly affect performance, energy, security/safety/reliability & scalability of computing platforms and applications. We rigorously understand and solve these challenges via novel techniques across the computing stack. To this end, we build hardware infrastructures (see cover figure) and follow two key directions.

**A.1. Fundamentally Better DRAM Architectures**

***
<div class="article-container">
  <div class="article">
    <img src="/public/apple-touch-icon.png" alt="Figure 1" class="article-image">
    <p class="article-description">
      Figure 1: Our Tesseract Processing in Memory system for Graph Processing (ISCA’15) provides more than 13X performance improvement and 8X energy reduction over state-of-the-art systems. Many works have been built on Tesseract, which provides a blueprint for future PIM systems.
    </p>
  </div>
  <div class="article">
    <img src="/public/apple-touch-icon.png" alt="Figure 2" class="article-image">
    <p class="article-description">
      Figure 2: Our bioinformatics work covers the entire genome analysis pipeline. Collectively, our algorithm-architecture co-design techniques provide >100X performance improvement & energy reduction over state-of-the-art systems. Figure replicated from our IEEE Micro 2020 invited paper “Accelerating Genome Analysis: A Primer on an Ongoing Journey”.
    </p>
  </div>
</div>


