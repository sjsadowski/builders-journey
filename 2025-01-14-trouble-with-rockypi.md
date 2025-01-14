---
title: The Trouble With RockyPi
slug: trouble-with-rockypi
description: Trials and tribulations of getting Rocky to boot on an RPi5
author: Stephen Sadowski
type: post
date: '2025-01-14T07:22:00.000-0500'
revisions:
draft: true
tags:
  - rpi
  - raspberrypi
  - rockylinux
  - linux
  - almalinux
preview:
category: tech
---

# The Trouble With RockyPi

> TL;DR: the Raspberry Pi SIG for Rocky Linux has not updated their image since 2022 and it
> does not contain the necessary boot firmware for Raspberry Pi 5. It works fine for all
> previous versions of 64-bit Raspberry Pi hardware (3, 3B, 3B+,  4B, 400, etc).

## A Rocky Start

I really like Rocky, and I love that the team is the spiritual successor to the original CentOS
project before [Big Purple](https://ibm.com/) got its grubby fingers on it and stomped it
into a mid-product replacement for RedHat Enterprise Linux Stream.

With much success I'd used Rocky on RPi 3B pluses and my RPi 4. While I do think that RedHat
has real issues with the community now, the tooling that they provide and support has always
been solid and stable. I've been RHCSA and RHCE certified in the past, and I use Fedora
as my daily driver(s) at home.

I started out by imaging the drives - Verbatim 2.5" Vi550 SSD 512Gb drives to be specific,
connected to the one of the USB 3.0 ports that support 5Gbps transfer. The drives support
500 MB/s write and 520 MB/s read, so the 5Gbps (625 MB/s) is pretty important so as to not
be the bottleneck.

The imaging process went fine and very quickly, no real issues.

> A note for the future: As of 2025/01/14 the Rocky aarch64 Raspberry Pu image
> does not, like others, run rootfs-expand on first boot. It is a manual effort.

Next steps were to connect it to the pi and power everything on. Unlike with the pi 4 and
it's switch to micro-HDMI, I was ready. I actually have a USB-HDMI power injector. On my pi4
this was necessary in order to get the signal boosted enough to be recognized.

With the power plugged in to the USB-C Power Delivery (pd) hub which is rated for 20W - below
spec for the RPi5, but most people say that this works fine, and it seems to initially.
The bootloader for the RPi5 states that it's negotiated 3A (3000 mA) but it seems to be booting
to the SSD no problem... except there is - while this isn't the exact issue I'm getting, it's
similar ([found here](https://forums.raspberrypi.com/viewtopic.php?t=370116))

```sh
type: 16 1ba: 8192 'mkfs.fat''v.   ^ ' clusters 36587 (16)
Trying partition: 0
type: 16 lba: 8192 mkfs.fat' ' v Boot mode: USB-MSD (04) order f
USB MSD stopped.Timeout: 25 seconds
Boot mode: RESTART (Of) order 0
Boot mode: SD (01) order f4
Trying partition: 0
type: 16 1ba: B192 'nkfs.fat' • V ^ ' clusters 36587 (16)
Trying partition: 9
type: 16 lba: 8192 'mkfs.fat' ' V ^ ' clusters 36587 (16)
Trying partition; 0
type: 16 1ba: 8192 'mkfs.fat' • V ^ ' clusters 36587 (16)
Trying partition: 0
type: 16 lba: 8192 'mkfs.fat' • v ^ ' clusters 36587 (16)
Boot mode: USB-MSD (04) order f ^ ' clusters 36587 (16)
```

And so the hunt begins. Mind you this hunt started on 2024/1/10, and 90% of the responses
about the Raspberry Pi 5 not booting Rocky Linux were related to the power: specifically
that the lack of power was causing the boot issue. The other 10% was that the image
was corrupted, and that needs to be reimaged. Since this was the lesser of the two
likely options, I put that path on hold and planned to get a RPi5 rated power supply.

In the mean time, I kept looking. And looking. And looking. Nearly everything said
it was a power issue, except nearly everything wasn't referencing Rocky. It
was things like Raspberry Pi OS, and in a few cases Windows... which surprised me -
People run Windows on RPis?

## I Cannae Get More Power

On 2025/1/12 my new 27w (5.1v/5a) power supply arrived. Unfortunately, I'd strained a
muscle in my back by doing snow shoveling and forgetting to lift with my legs a couple of
days prior. I was surviving on naproxen and ibuprofen, but then we got more snow and ended up
doing a Britney Spears (oops! I did it again), this time straining the muscle completely.

So I was down for the count, and the next day saw me with a doctor's visit, pain killers
and a muscle relaxer. I wasn't very useful to myself or others. Most of the day on 2025/1/13
was shot but by evening I was coherent enough to give the new power supply a go.

...and it failed. Not the power supply - that was fine - but the boot issue remained. Alright,
then, imaging time. 20 minutes later, RPi is re-imaged and... nothing changed.

Well one thing changed: it recognized the power supply as 5000mA




